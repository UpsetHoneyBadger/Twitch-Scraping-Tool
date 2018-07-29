import requests
import json
from client_secret import client_secret

headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-ID': client_secret
}

r = requests.get('https://api.twitch.tv/kraken/users?login=dallas,dallasnchains', headers=headers)

print(r.json())