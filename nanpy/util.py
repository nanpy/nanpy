

def constrain(value, xmin, xmax):
    if value < xmin:
        return xmin
    if value > xmax:
        return xmax
    return value

