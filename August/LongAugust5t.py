import math
T = input()
t = int(T)
for i in range(t):
    l = list(map(int, input().split()))
    members = list(map(int, input().split()))
    n = int(l[0])
    k = int(l[1])
    arguements = {}
    for i in range(len(members)):
        if members[i] in arguements:
            arguements[members[i]] += 1
        else:
            arguements[members[i]] = 1

    def get_repeatDict(arr):
        arguements = {}
        for i in range(len(arr)):
            if arr[i] in arguements:
                arguements[arr[i]] += 1
            else:
                arguements[arr[i]] = 1
        return arguements

    def get_sum(arr):
        arguements = get_repeatDict(arr)
        least_eff = 0
        for val in arguements.values():
            if val > 1:
                least_eff += val
        return least_eff

    def get_least_eff(arr):
        arguements = get_repeatDict(arr)
        least_eff = k
        for val in arguements.values():
            if val > 1:
                least_eff += val
        return least_eff

    def minimumSubarrays(ar, n):
        se = []

        cnt = 1

        for i in range(n):
            if se.count(ar[i]) == 0:

                # inserting the current element
                se.append(ar[i])
            else:
                cnt += 1

                # clear set for new possible value
                # of subarrays
                se.clear()

                # inserting the current element
                se.append(ar[i])
        return cnt

    def nextMinimumSubarray(arr, n):
        se = []
        for i in range(n):
            if se.count(arr[i]) == 0:
                se.append(arr[i])
            else:
                return [se, i]
        return [se, i]
    thisset = set()
    se = []
    arr = []
    cnt = 1
    temp = []
    temp1 = []
    remainder = 0
    for i in range(len(members)):
        arr.append(members[i])
    i = 0

    re = 0
    left_index = 0
    while i < n:
        temp = []
        for j in range(i, n):
            temp.append(arr[j])
        subarray = nextMinimumSubarray(temp, len(temp))[0]
        left_subarray = []
        for j in range(left_index, i):
            left_subarray.append(arr[j])
        right_subarray = []
        for j in range(i+len(subarray), n):
            right_subarray.append(arr[j])
        left_save, right_save = 0, 0
        for j in subarray:
            if left_subarray.count(j) == 1:
                left_save = 2 + left_save
            elif left_subarray.count(j) > 1:
                left_save += 1
        for j in subarray:
            if right_subarray.count(j) == 1:
                right_save += 2
            elif right_subarray.count(j) > 1:
                right_save += 1
        flag = 0
        print(subarray, left_subarray, right_subarray, cnt)
        if left_save > k:
            flag = 1
            cnt += 1
            remainder = remainder + get_least_eff(left_subarray) - k
            left_index = left_index + len(left_subarray)
            ultra_temp = []
            for j in range(len(subarray)):
                ultra_temp.append(subarray[j])
            ultra_temp.extend(right_subarray)
            re = get_least_eff(ultra_temp) - k
        if right_save > k:
            cnt += 1
            ultra_temp = []
            for j in range(len(left_subarray)):
                ultra_temp.append(left_subarray[j])
            ultra_temp.extend(subarray)
            if flag == 0:
                remainder = remainder + get_least_eff(ultra_temp) - k
            else:
                remainder = remainder + get_least_eff(subarray) - k
            re = get_least_eff(right_subarray) - k
            if flag == 1:
                left_index = left_index+len(subarray)
            else:
                left_index += len(subarray) + len(left_subarray)
        i += len(subarray)
    count = cnt
    print(count, remainder, re)
    if count == 1 and k != 1:
        print(get_least_eff(members))
    else:
        print((count*k)+remainder+re)
