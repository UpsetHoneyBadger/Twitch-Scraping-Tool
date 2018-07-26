import requests
import json


headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-ID': 'ndv731ys6v4rpbe4n5jdpofzxju3jv'
}

r = requests.get('https://api.twitch.tv/kraken/users?login=dallas,dallasnchains', headers=headers)

print(r.json())