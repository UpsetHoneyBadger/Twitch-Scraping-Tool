import requests
import json
import csv
from datetime import datetime
with open("./client_secret.txt") as file:
    client_secret = file.read()


r = requests.get('http://tmi.twitch.tv/group/user/eleaguetv/chatters')
# print(r.json().keys())

viewers =  r.json()['chatters']['viewers']

# make chunks for viewer requests
chunks = [viewers[idx * 100 : (idx+1) * 100] for idx in range(0, len(viewers) // 100)]
lastChunk = viewers[len(viewers) // 100 * 100 : len(viewers)]
chunks.append(lastChunk)

# build headers
headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-ID': client_secret
}

viewer_info = list()
for chunk in chunks:
    response = requests.get('https://api.twitch.tv/kraken/users?login=' + ','.join(chunk), headers=headers)
    # print(response.json()['users'][0])
    viewer_info = viewer_info + response.json()['users']
print(len(viewer_info))

with open('./viewer_info_' + datetime.now().strftime('%Y.%m.%d_%H.%M.%S') + '.csv', 'w', encoding='utf-8', newline='') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, viewer_info[0].keys())
    w.writeheader()
    w.writerows(viewer_info)
    # for user in viewer_info:
        # w.writerow(user)


# print(len(viewers))
# print(viewer_info.json()['users'][0:5])
# print(len(chunks[-1]))