def allnum(strlist):
    i = 0
    allnum_strlist = []
    for num in strlist:
        if num.isdigit():
            allnum_strlist.append(num)
    return allnum_strlist