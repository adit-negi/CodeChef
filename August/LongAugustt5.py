
import math
T = input()
t = int(T)
for i in range(t):
    l = list(map(int, input().split()))
    members = list(map(int, input().split()))
    N = int(l[0])
    k = int(l[1])

    def get_subarray(index, arr):
        se = []
        for i in range(index, len(arr)):
            if se.count(arr[i]) == 0:
                se.append(arr[i])
            else:
                return se
        return se

    def count_subarray(arr):
        se = []
        count = 1
        for i in range(len(arr)):
            if se.count(arr[i]) == 0:
                se.append(arr[i])
            else:
                count += 1
                se.clear()
                se.append(arr[i])
        return count

    def get_repeatDict(arr):
        arguements = {}
        for i in range(len(arr)):
            if arr[i] in arguements:
                arguements[arr[i]] += 1
            else:
                arguements[arr[i]] = 1
        return arguements

    def get_least_eff(arr):
        arguements = get_repeatDict(arr)
        least_eff = k
        for val in arguements.values():
            if val > 1:
                least_eff += val
        return least_eff

    def nextMinimumSubarray(arr, index):
        se = []
        for i in range(index, len(arr)):
            if se.count(arr[i]) == 0:
                se.append(arr[i])
            else:
                return se
        return se

    arr = []
    for i in range(len(members)):
        arr.append(members[i])

    temp = []
    thisset = set()
    max_possible = get_least_eff(arr)
    cost = 0
    t = [[-1 for i in range(len(arr) + 1)] for j in range(N+1)]

    def cheftables(arr, n, count):
        if n >= len(arr) or arr == [] or count >= N:
            return get_least_eff(arr)
        left_array = []
        if t[n][len(arr)] != -1:
            return t[n][len(arr)]
        for i in range(n):
            left_array.append(arr[i])
        right_array = arr[n:]
        t[n][len(arr)] = min(get_least_eff(left_array) +
                             cheftables(right_array, 1, count+1),  cheftables(arr, n+1, count+1))
        return t[n][len(arr)]

    remainder = 0

    se = []

    cnt = 1

    total_cost_yet = get_least_eff(members)
    n = N
    for i in range(n):
        if arr[i] not in thisset:
            thisset.add(arr[i])
            se.append(arr[i])
        else:
            temp = []
            for j in range(i, n):
                temp.append(arr[j])
            total_new_cost = get_least_eff(se)+get_least_eff(temp)
            if k == 1:
                if total_new_cost <= total_cost_yet:
                    cnt = cnt+1
                    total_cost_yet = get_least_eff(temp)
                    se.clear()
                    thisset.clear()
                    remainder = get_least_eff(temp)-k
                    se.append(arr[i])
                    thisset.add(arr[i])
                else:
                    break
            else:
                if total_new_cost < total_cost_yet:
                    cnt = cnt+1
                    total_cost_yet = get_least_eff(temp)
                    se.clear()
                    thisset.clear()
                    remainder = get_least_eff(temp)-k
                    se.append(arr[i])
                    thisset.add(arr[i])
                else:
                    break

    count = cnt
    if k == 1:
        print(count_subarray(members))
    else:
        try:
            print(cheftables(arr, 1, 0))
        except Exception as e:
            if count == 1 and k != 1:
                print(get_least_eff(members))
            else:
                print((count*k)+remainder)
