import requests
# from optparse import OptionParser
from database_functions import store_viewers_to_table, store_viewers_to_table_array
from scan_list import streamer_names
# parser = OptionParser()

# parser.add_option("-F", "--file", dest="file_name", default="scan_list.txt",
#                   help="file name with the list of streamers that  should be scanned"
#                  )
# parser.add_option("-L", "--limit", dest="limit", default=10,
#                   help="amount of streamers to scan (ordered by most viewers), default=10"
#                   )

# (options, args) = parser.parse_args()

# with open(options.file_name) as file:
#     streamer_names = [line.rstrip('\n') for line in file.readlines()]
print(streamer_names)
for name in streamer_names:
    r = requests.get('http://tmi.twitch.tv/group/user/' + name.lower() + '/chatters')
    viewers =  r.json()['chatters']['viewers']

    print('streamer name =', name)
    # print('amount of viewers =', name['viewer_count'])
    print('viewers in chat =', len(viewers))#, '('+ str(round(len(viewers) / name['viewer_count'] * 100, 1)) +'%)')
    # store viewer array in a database here
    store_viewers_to_table_array(name, viewers)