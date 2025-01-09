def cycle(input_list):
    new_list = input_list.copy()
    a = [new_list[0]]
    new_list.pop(0)
    new_list.extend(a)
    return new_list