import n_queens

n = 5
b = [[False] * n for i in range(n)]

n_queens.queens(b, 0, n)