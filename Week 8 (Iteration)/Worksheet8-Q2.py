text = input("Enter the list of words: ")
suffix = input("Enter the common suffix: ")
text = text.split()
for word in text:
    word = word + suffix
    print(word)