def friend_besties(individual, bestie_dict):
    newlist = []
    if individual not in bestie_dict.keys():
        return newlist
    elif individual in bestie_dict.keys():
        for person in bestie_dict[individual]:
            newlist.append(person)
    newlist = sorted(newlist)
    return newlist
