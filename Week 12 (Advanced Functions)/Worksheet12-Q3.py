def issorted(numlist):
    for i in range(1, len(numlist)):
        if numlist[i] < numlist[i - 1]:
            return False
    return True
