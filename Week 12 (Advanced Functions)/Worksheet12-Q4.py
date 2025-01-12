def basenum(num, base):
    num = str(num)
    for digit in num:
        if int(digit) >= base:
            return False
    return True