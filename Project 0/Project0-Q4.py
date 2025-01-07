def least_vowel_words(text):
    punctuation = ",.:;!?\"'-"
    cleaned_words = []
    for word in text.split():
        word = word.rstrip(punctuation).lower()
        if len(word) > 0:
            cleaned_words.append(word)

    lowest_vowel = 1
    result = []
    for word in cleaned_words:
        count = 0
        for char in word:
            if char in 'aeiou':
                count += 1
        lowest_ratio = count / len(word)
        if lowest_ratio < lowest_vowel:
            lowest_vowel = lowest_ratio
            result = [word]
        elif lowest_ratio == lowest_vowel and word not in result:
            result.append(word)
    return result


