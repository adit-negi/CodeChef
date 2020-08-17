T = input()
t = int(T)

for i in range(t):
    N = input()
    n = int(N)
    M = [[0 for i in range(n)] for j in range(n)]
    number = 1
    for i in range(n):
        for j in range(n):
            M[i][j] = number
            number = number+1
    if n % 2 == 0:
        for i in range(1, n, 2):
            j = 0
            while j < n-1:
                temp = M[i][j]
                M[i][j] = M[i][j+1]
                M[i][j+1] = temp
                j = j+2

    print(M)
