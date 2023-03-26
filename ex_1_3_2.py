n, k = map(int, input().split())


def c(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        res = c(n - 1, k) + c(n - 1, k - 1)
        return res


print(c(n, k))
