def f(x):
    return ((x)**2) - 1

def find_min(function, start = -1 , end = 1, step = 0.1):
    minimum = 1e10
    while start <= end:
        if function(start) < minimum:
            minimum = f(start)
        start += step
    return minimum