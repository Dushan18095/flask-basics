def number_of_digits(n):
    m = 0
    while n > 0:
        n = n // 10
        m += 1
    return m

def factorize(n):
    factors = []
    f = 2
    while n >= f:
        if n % f == 0:
            factors.append(f)
            n = n / f
        else:
            f = f + 1
    return factors

