import requests
from client_secret import client_secret

def get_streamer_metadata(channel_name):
    headers = {
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Client-ID': client_secret
    }
    r = requests.get('https://api.twitch.tv/kraken/users?login=' + channel_name, headers=headers)
    channel_id = r.json()['users'][0]['_id']
    r = requests.get('https://api.twitch.tv/kraken/streams/' + str(channel_id), headers=headers)
    print(r.json())
    

if __name__ == '__main__':
    get_streamer_metadata('asmongold')