def validate_card(number):
    sum = 0
    if number.isdigit():
        if len(number) == 16:
            for i in range(0,len(number)):
                 sum = sum + int(number[i])
            if sum%10 == 0:
                 return True
            else:
                 return False
        return False
    return False