from collections import defaultdict

def approximate_song(filename):
    wordcount = defaultdict(int)

    fp = open(filename, 'r')
    content = fp.read()
    fp.close()

    content = content.split()
    for word in content:
        wordcount[word] += 1

    wordcount = sorted(wordcount, key=lambda item: (-wordcount[item], item))
    return wordcount[0]