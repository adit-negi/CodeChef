import itertools
T = input()
t = int(T)

for i in range(t):
    N = int(input())
    X = list(map(int, input().split()))
    L = []
    close = []
    far = []
    for i in range(len(X)-1):
        a = abs(X[i+1]-X[i])
        if a == 2 or a == 1:

            L.append(1)
        elif a > 2:
            L.append(3)
    close = [len(list(g)) for k, g in itertools.groupby(L) if k == 1]
    far = [len(list(g)) for k, g in itertools.groupby(L) if k == 3]

    if X[N-1]-X[N-2] > 2 or X[1]-X[0] > 2:
        if len(close) == 0:
            print(1, 1)
            break
        else:
            print(1, max(close)+1)
            break
    if len(far) == 0:
        print(max(close)+1, max(close)+1)
        break
    if max(far) > 1 and len(close) > 0:
        print(1, max(close)+1)
        break
    if max(far) > 1 and len(close) == 0:
        print(1, 1)
        break
    if max(far) == 1 and len(close) > 0:
        print(min(close)+1, max(close)+1)
        break
    if max(far) == 1 and len(close) == 0:
        print(1, 1)
        break
