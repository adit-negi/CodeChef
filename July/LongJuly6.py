import math
T = input()
t = int(T)
for i in range(t):
    NX = list(map(int, input().split()))
    N = int(NX[0])
    X = int(NX[1])
    A = list(map(int, input().split()))
    total = 0
    A.sort()
    x = X
    for i in range(N):
        if A[i] > X/2 and A[i] < X:
            x = A[i]
            break
    for i in range(N):
        if A[i] > X/2:
            days = math.ceil(A[i]/x)
            if x <= A[i]:
                Ax = days
                day_it_doubles = math.ceil((math.log(Ax, 2))) + 1
            else:
                day_it_doubles = 1

            x = 2*A[i]

            total = total+day_it_doubles
        else:
            total = total + 1

    print(total)
