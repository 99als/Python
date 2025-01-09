def repeat_word_count(text, n):
    wordcount = {}
    new_list = []
    text = text.split()
    for word in text:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    for key, value in wordcount.items():
        if value >= n:
            new_list.append(key)
    new_list = sorted(new_list)
    return new_list