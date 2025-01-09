def mode(numlist):
    numcount = {}
    new_numlist = []

    for num in numlist:
        if num in numcount:
            numcount[num] += 1
        else:
            numcount[num] = 1

    biggest_val = 0
    for value in numcount.values():
        if value > biggest_val:
            biggest_val = value

    for key, value in numcount.items():
        if value == biggest_val:
            new_numlist.append(key)

    new_numlist = sorted(new_numlist)
    return new_numlist