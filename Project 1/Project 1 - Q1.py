def get_friendly_dict(friend_list):
    newdict = {}
    for friend1, friend2 in friend_list:
        if friend1 not in newdict:
            newdict[friend1] = set()
        if friend2 not in newdict:
            newdict[friend2] = set()
        if friend1 in newdict:
            newdict[friend1].add(friend2)
        if friend2 in newdict:
            newdict[friend2].add(friend1)
    return newdict
