word = input("Hit me: ")
word = '^' + word + '$'
if ('omics$' in word):
    print("Life science hippy!")
elif ('^comp' in word or '^info' in word):
    print("Computing ftw!")
elif ('y$' in word):
    print("Au naturel!")
else:
    print("Too new to keep up!")