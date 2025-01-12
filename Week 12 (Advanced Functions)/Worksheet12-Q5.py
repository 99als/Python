def top5_words(text):
    text = text.split()
    my_dict = {}
    for word in text:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    my_dict = sorted(my_dict, key=lambda item: (-my_dict[item], item))
    return my_dict[: 5]