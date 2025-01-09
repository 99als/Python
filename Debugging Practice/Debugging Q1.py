def hyphenate_words(string):
    words = []
    for word in string.split():
        word = list(word)
        hyphenated = '-'.join(word)
        words.append(hyphenated)

    return ' '.join(words)