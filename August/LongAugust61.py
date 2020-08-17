import math
import itertools
import operator as op
from functools import reduce

T = input()
t = int(T)
for i in range(t):
    n = int(input())
    L = list(map(int, input().split()))
    dict_ = {}
    count = 0
    for i in range(n):
        if L[i] in dict_:

            dict_[L[i]] += 1
        else:
            dict_[L[i]] = 1
            count = count+1

    l = [0]*n

    def ncr(n, r):
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer // denom

    for key in dict_:

        count_of_key = dict_[key]
        key_occurences = 0
        count_of_tempkey = 1
        for i in range(count_of_key):
            total = 1
            for temp_key in dict_:
                sum_of_key = 1
                if temp_key != key:
                    count_of_tempkey = dict_[temp_key]

                    if temp_key > key:
                        times_it_can_appear = min(i+1, count_of_tempkey)
                    else:
                        times_it_can_appear = min(i, count_of_tempkey)
                    for j in range(times_it_can_appear):
                        sum_of_key += ncr(count_of_tempkey, j+1)
                total = total*sum_of_key

            key_occurences += total*ncr(count_of_key, i+1)

        l[key-1] = key_occurences
    print(*l)


# for temp_key in dict_:
#             sum_of_key = 1
#             if temp_key != key:
#                 count_of_tempkey = dict_[temp_key]

#                 if temp_key > key:
#                     times_it_can_appear = min(count_of_key-1, count_of_tempkey)
#                 else:
#                     times_it_can_appear = min(count_of_key, count_of_tempkey)
#                 for j in range(times_it_can_appear):
#                     sum_of_key += ncr(count_of_tempkey, j+1)
#             total = total*sum_of_key
