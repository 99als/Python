def wordlist(text):
    alpha = []
    text = text.split()
    for word in text:
        if word.isalnum():
            alpha.append(word)
        else:
            break
    return alpha