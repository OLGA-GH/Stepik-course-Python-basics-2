def closest_mod_5(x):
    if x % 5 == 0:
        return x
    for y in range(x, x + 5):
        if y % 5 == 0:
            return y
