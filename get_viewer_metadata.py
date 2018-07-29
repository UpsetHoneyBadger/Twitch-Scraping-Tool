def get_user_metadata(viewers):
    # filter out viewer who are already in the DB
    known_users = ['steven', 'frank']
    unique_users = list()

    for user in viewers:
        if user not in known_users:
            unique_users.append(user)


    print(unique_users)

    # API request to twitch to find metadata from unknown viewers

    # store unknown metadata to database


if __name__ == "__main__":
    get_user_metadata(['peter', 'steven', 'mike'])