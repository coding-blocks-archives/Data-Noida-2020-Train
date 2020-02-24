def pd(n):
    if n == 0:
        return

    print(n)
    pd(n-1)

pd(5)