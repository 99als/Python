def middle_words(word_list):
    new_list = []
    if len(word_list) % 2 != 0:
        middle = int(len(word_list) / 2)
        new_list.append(word_list[middle])
    else:
        middleleft = int(len(word_list) / 2) - 1
        middleright = int(len(word_list) / 2)
        new_list.append(word_list[middleleft])
        new_list.append(word_list[middleright])
    return new_list

