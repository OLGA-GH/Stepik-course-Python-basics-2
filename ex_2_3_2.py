def primes():
    def is_simple(n):
        counter = 0
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                counter += 1
        if counter == 0:
            return True

    n = 2
    while True:
        if is_simple(n):
            yield n
        n += 1
