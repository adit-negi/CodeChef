from collections import Counter
import operator as op
from functools import reduce
t = int(input())
for i in range(t):
    L = list(map(int, input().split()))
    N = int(L[0])
    C = int(L[1])
    K = int(L[2])
    c = []
    for i in range(N):
        lines = list(map(int, input().split()))
        c.append(lines[2])
    VC = list(map(int, input().split()))
    Vc = int(VC[0])
    temp = []
    count = Counter(c)
    for i in range(1, C+1):
        if count[i] >= 3:
            temp.append(count[i])
    removeable_lines = int(K/Vc)
    temp.sort(reverse=True)
    j = 0

    for i in range(removeable_lines):
        temp[temp.index(max(temp))] -= 1

    def ncr(n, r):
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer // denom
    triangles = 0
    for i in temp:
        if i >= 3:
            triangles = triangles + ncr(i, 3)
    print(triangles)
