import requests
with open("./client_secret.txt") as file:
    client_secret = file.read()

def get_top_streamers(limit=10):
    headers = {
        'Client-ID': client_secret
    }
    if limit <= 100:
        r = requests.get('https://api.twitch.tv/helix/streams?first='+ str(limit), headers=headers)
        streamer_data = r.json()['data']
    else:
        # pagination stuff
        streamer_data = list()
        cursor = ''
        
        while(len(streamer_data) < limit):
            headers = {
                'Client-ID': client_secret
            }
            request_url = 'https://api.twitch.tv/helix/streams?first=100' + ('&after=' + cursor if cursor != '' else '')
            r = requests.get(request_url, headers=headers)
            streamer_data = streamer_data + r.json()['data']
            cursor = r.json()['pagination']['cursor']
    # get user ids of the streamers
    streamer_ids = [streamer['user_id'] for streamer in streamer_data]
    # make chunks for user-id requests   
    chunks = [streamer_ids[idx * 100 : (idx+1) * 100] for idx in range(0, len(streamer_ids) // 100)]
    lastChunk = streamer_ids[len(streamer_ids) // 100 * 100 : len(streamer_ids)]
    if(len(lastChunk) > 0):
        chunks.append(lastChunk)
    headers = {
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Client-ID': 'ndv731ys6v4rpbe4n5jdpofzxju3jv'
    }
    streamer_names = list()
    for chunk in chunks:
        # print('https://api.twitch.tv/helix/users?id=' + '&id='.join(chunk))
        response = requests.get('https://api.twitch.tv/helix/users?id=' + '&id='.join(chunk), headers=headers)
        streamer_names = streamer_names + [streamer_info['login'] for streamer_info in response.json()['data']]
    top_streamers = [
        {
            'user_name': streamer_names[i],
            'viewer_count': streamer_data[i]['viewer_count']
        }
        for i in range(len(streamer_data))
    ]
    return top_streamers[0:limit]

if __name__ == "__main__":
    top_streamers = get_top_streamers(100)
    print(len(top_streamers))
    # print(top_streamers)