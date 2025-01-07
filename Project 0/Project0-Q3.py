def symmetric_words(wlist):
    symmetricList = []
    for word in wlist:
        boolCheck = False
        if len(word)%2 == 0:
            for i in range(0, len(word)):
                if ord(word[i]) > 109:
                    if (ord('z') - ord(word[i]) == ord(word[len(word) - 1 - i]) - ord('a')):
                        boolCheck = True
                    else:
                        boolCheck = False
        if boolCheck:
            symmetricList.append(word)
    symmetricList.sort()
    return symmetricList


