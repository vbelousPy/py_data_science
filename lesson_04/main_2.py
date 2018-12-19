def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def combination(n, k):
    nf = factorial(n)
    kf = factorial(k)
    diff = factorial(n - k)

    return nf // (kf * diff)


print(combination(42, 6))
