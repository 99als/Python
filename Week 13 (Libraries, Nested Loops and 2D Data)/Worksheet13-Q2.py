from collections import defaultdict

def count_lengths(text):
    countdict = defaultdict(int)
    text = text.split()
    for word in text:
        countdict[len(word)] += 1
    return countdict

def top5_word_lengths(text):
    top5dict = count_lengths(text)
    top5dict = sorted(top5dict, key=lambda item: (-top5dict[item], -item))
    return top5dict[:5]