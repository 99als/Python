def unique_long_words(wlist, wlen):
    count = 0
    uniqueList = []
    for word in wlist:
        if len(word) >= wlen and word not in uniqueList:
            count += 1
            uniqueList.append(word)
    return count