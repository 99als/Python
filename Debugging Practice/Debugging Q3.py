def combine(num1, num2, add):
    ''' If add == True,  return num1+num2
        If add == False, return num1*num2 '''

    # First check that add is a boolean for safety
    if add != False and add != True:
        return None

    if add:
        return num1 + num2
    else:
        return num1 * num2