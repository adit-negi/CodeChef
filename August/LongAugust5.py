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
    thisset = set()
    iset = set()

    remainder = 0

    se = []

    cnt = 1
    arr = []
    for i in range(len(members)):
        arr.append(members[i])

    total_cost_yet = get_least_eff(members)

    for i in range(n):
        if arr[i] not in thisset:
            thisset.add(arr[i])
            se.append(arr[i])
        else:
            temp = []
            for j in range(i, n):
                temp.append(arr[j])

            total_new_cost = k + get_least_eff(temp)

            if total_new_cost <= total_cost_yet:
                cnt = cnt+1
                total_cost_yet = get_least_eff(temp)
                se.clear()
                thisset.clear()
                remainder = get_least_eff(temp)-k
                se.append(arr[i])
                thisset.add(arr[i])

            else:
                secondary = minimumSubarrays(temp, len(temp))*k + k
                if secondary <= total_cost_yet:
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
    print(count)
    if count == 1 and k != 1:
        print(get_least_eff(members))
    else:
        print((count*k)+remainder)
