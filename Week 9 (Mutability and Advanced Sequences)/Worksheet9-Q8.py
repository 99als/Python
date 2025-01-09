def long_high_word(wordlist):
    highestLength = len(wordlist[0])
    bigWord = ""
    for word in wordlist:
        if len(word) > highestLength:
            bigWord = word
            highestLength = len(word)
        if len(word) == highestLength:
            if word > bigWord:
                bigWord = word
    return bigWords