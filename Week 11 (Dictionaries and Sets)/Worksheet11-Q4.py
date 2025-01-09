def top5_words(text):
    text = text.split(" ")
    wordcount = {}
    sortedwords = []
    new_list = []
    # get items into dict
    for word in text:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    # sort the dict
    for key, value in wordcount.items():
        sortedwords.append((-value, key))
    sortedwords = sorted(sortedwords)

    # iterate through the top 5 values, in descending order
    if len(sortedwords) < 5:
        for i in range(0, len(sortedwords)):
            new_list.append(sortedwords[i][1])
    else:
        for i in range(0, 5):
            new_list.append(sortedwords[i][1])

    return new_list