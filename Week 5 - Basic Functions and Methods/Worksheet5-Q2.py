def canner_can2(item):
    """" canner_can takes a string item (assumed to be an animal) and returns a string containing an important question about the animal """
    # write your code here
    if (item == ""):
        return "Can you can a " + item + " as a canner can can a can?"
    newItem = item.lower()
    if (newItem[0] in 'aeiou'):
        return "Can you can an " + item + " as a canner can can a can?"
    else:
        return "Can you can a " + item + " as a canner can can a can?"

