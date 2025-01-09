def mutual_friends(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return len(set1&set2)