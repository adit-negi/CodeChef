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

    def cheftables(arr, n):
        if n >= len(arr) or arr == []:
            return get_least_eff(arr)

        left_array = []
        if t[n][len(arr)] != -1:
            return t[n][len(arr)]

        subarray = nextMinimumSubarray(arr, n)
        for i in range(n+len(subarray)):
            left_array.append(arr[i])
        right_array = arr[n+len(subarray):]
        t[n][len(arr)] = min(get_least_eff(left_array) +
                             cheftables(right_array, 0),  cheftables(arr, n+1))
        return t[n][len(arr)]
    print(cheftables(arr, 0))


# import math
# T = input()
# t = int(T)
# for i in range(t):
#     l = list(map(int, input().split()))
#     members = list(map(int, input().split()))
#     N = int(l[0])
#     k = int(l[1])

#     def get_subarray(index, arr):
#         se = []
#         for i in range(index, len(arr)):
#             if se.count(arr[i]) == 0:
#                 se.append(arr[i])
#             else:
#                 return se
#         return se

#     def get_repeatDict(arr):
#         arguements = {}
#         for i in range(len(arr)):
#             if arr[i] in arguements:
#                 arguements[arr[i]] += 1
#             else:
#                 arguements[arr[i]] = 1
#         return arguements

#     def get_least_eff(arr):
#         arguements = get_repeatDict(arr)
#         least_eff = k
#         for val in arguements.values():
#             if val > 1:
#                 least_eff += val
#         return least_eff

#     def nextMinimumSubarray(arr, index):
#         se = []
#         for i in range(index, len(arr)):
#             if se.count(arr[i]) == 0:
#                 se.append(arr[i])
#             else:
#                 return se
#         return se

#     arr = []
#     for i in range(len(members)):
#         arr.append(members[i])

#     temp = []
#     thisset = set()
#     max_possible = get_least_eff(arr)
#     cost = 0

#     def cheftables(arr, n):
#         if n >= len(arr) or arr == []:
#             return get_least_eff(arr)
#         left_array = []
#         subarray = nextMinimumSubarray(arr, n)
#         print(n, subarray)
#         for i in range(n+len(subarray)):
#             left_array.append(arr[i])
#         right_array = arr[n+len(subarray):]
#         return min(get_least_eff(left_array) + cheftables(right_array, 0),  cheftables(arr, n+1))
#     print(cheftables(arr, 0))
