def check_csc(code):
    if len(code) != 3:
        return False
    else:
        if code.isdigit():
            return True
        else:
            return False