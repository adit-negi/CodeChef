import itertools


import math
# T = input()
# t = int(T)
# for i in range(t):
#     n = int(input())
#     L = list(map(int, input().split()))
#     dict_ = {}

#     def power(x, y):
#         res = 1
#         while (y > 0):

#             if ((y & 1) == 1):
#                 res = res * x
#             y = y >> 1

#             x = x * x

#         return res
#     l = []
#     for i in range(1, n+1):
#         l.append(pow(2, n-i, 23375247598357347583))
#     print(*l)
dict_ = {}


def Sub_Sequences(STR):
    combs = []
    for l in range(1, len(STR)+1):
        combs.append(list(itertools.combinations(STR, l)))
    for c in combs:
        for t in c:
            if t is not None:
                print(t)
                temp = min(t)
                if temp in dict_:
                    dict_[temp] += 1
                else:
                    dict_[temp] = 1
    return dict_


countDict = Sub_Sequences([1, 2, 3, 4])
print(countDict)
l = []
for i in range(1, 3+1):
    if i in countDict:
        l.append(countDict[i] % 1000000007)
    else:
        l.append(0)

print(*l)
