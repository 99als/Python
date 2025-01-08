def make_gamertag(name):
    new_name = ""
    for i in range(0,len(name)):
        new_name = new_name + name[i] + '-'
    return new_name