def longest_sentence_length(text):
    text = text.split('.')
    count = 0
    for word in text:
        big = len(word.split())
        if big > count:
            count = big
    return count