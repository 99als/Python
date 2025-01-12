def matching_codons(complements, pool1, pool2):
    matchingset = []
    for item in pool1:
        match = ""
        for char in item:
            if char in complements:
                match += complements[char]
        if match in pool2:
            matchingset.append((item,match))
    return matchingset
