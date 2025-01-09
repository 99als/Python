def sorted_words(wordlist):
    sortedwords = []
    sort = ()
    for word in wordlist:
        checkword = ''
        checkword = checkword.join(sorted(word))
        if checkword == word:
            sortedwords.append(word)

    return sorted(sortedwords)