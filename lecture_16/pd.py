def pd(n):

    if n == 0:
        return

    print(n)
    pd(n-1)

def pi(n):

    if n == 0:
        return

    pi(n-1)
    print(n)

def pdi(n):

    if n == 0:
        return

    print(n)
    pdi(n-1)
    print(n)


pdi(5)