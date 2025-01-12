def maxby(intlist):
    if intlist:
        if len(intlist) == 1:
            return (intlist[0], None)
        else:
            first_biggest_num = max(intlist)
            intlist.remove(first_biggest_num)
            second_biggest_num = max(intlist)
            difference = first_biggest_num - second_biggest_num
            return (first_biggest_num, difference)
    else:
        return (None, None)
