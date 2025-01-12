def grey_value(image):
    totalcount = 0
    whiteimage = 0
    for coord in image:
        for value in coord:
            if value == 1:
                whiteimage += 1
                totalcount += 1
            else:
                totalcount += 1
    return whiteimage / totalcount


