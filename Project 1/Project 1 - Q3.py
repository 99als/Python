def friend_second_besties(individual, bestie_dict):
    newlist = []
    # get the individual and find which friend group they are in
    # cross compare against their friend group (maybe use a set difference)???

    for friend, friend_group in bestie_dict.items():
        if individual in friend_group:
            for friends in friend_group:
                if friends not in bestie_dict[individual]:
                    if friends != individual:
                        newlist.append(friends)
    newlist = sorted(newlist)
    return newlist