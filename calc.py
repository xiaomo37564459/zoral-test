def power(base, exp):
    if exp < 0:
        raise ValueError("exp must be >= 0")
    return base ** exp
