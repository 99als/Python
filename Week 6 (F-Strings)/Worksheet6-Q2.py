def dodgy_inventorise(item):
    volume = item[0]
    name = item[1]
    total = item[2]
    return f"{volume:<6}{name:>20.20s}{total:>10.2f}"