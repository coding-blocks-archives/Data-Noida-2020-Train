def fibo(n):
    if n < 2:
        return n

    first = fibo(n-1)
    second = fibo(n-2)

    total = first + second
    return total


def fiboDP(n, memory):
    if n < 2:
        return n

    if memory.get(n):
        return memory.get(n)

    first = fiboDP(n - 1, memory)
    second = fiboDP(n - 2, memory)

    total = first + second
    memory[n] = total

    return total


print(fiboDP(50, {}))

