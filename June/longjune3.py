T = input()
t = int(T)

for i in range(t):
    total_people = int(input())
    coins = list(map(int, input().split()))
    L = [0, 0, 0]
    flag = 0
    for i in range(total_people):
        if coins[i] == 5:
            L[0] = L[0]+1
        elif coins[i] == 10:
            if L[0] > 0:
                L[1] = L[1]+1
                L[0] = L[0]-1
            elif L[0] == 0:
                flag = 1
                break
        elif coins[i] == 15:
            if L[1] > 0:
                L[1] = L[1]-1
            elif L[0] > 1:
                L[0] = L[0]-2
            elif (L[0] == 0 or L[0] == 1) and (L[1] == 0):
                flag = 1
                break
 
    if flag == 0:
        print('YES')
    if flag == 1:
        print('NO')
