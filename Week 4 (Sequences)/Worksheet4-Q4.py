phrase = input("Enter a phrase: ")
checkphrase = phrase.lower()
if (len(phrase) > 0):
    isVowel = checkphrase[0]
    if (isVowel in 'aeiou'):
        print("an " + phrase)
    else:
        print("a " + phrase)

else:
    print("a " + phrase)
