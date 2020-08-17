T = input()
t = int(T)
j = 0
for i in range(t):
    N = int(input())
    Q = list(map(int, input().split()))
    l = []
    covid = 0
    for j in range(N):
        if Q[j] == 1:
            l.append(j)
    for j in range(len(l)-1):
        if l[j+1] - l[j] < 6:
            covid = 1

    if covid == 0:
        print('YES')
    else:
        print("NO")
