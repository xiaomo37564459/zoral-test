def clamp(x, lo, hi):
    if lo > hi:
        raise ValueError("lo must not be greater than hi")
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x
