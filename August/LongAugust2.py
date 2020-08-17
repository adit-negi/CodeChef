T = input()
t = int(T)
for i in range(t):
    l = list(map(int, input().split()))
    Opponents = list(map(int, input().split()))
    n = int(l[0])
    k = int(l[1])  # chefs pawn
    L = []
    for i in range(n):
        if k % Opponents[i] == 0:
            L.append(Opponents[i])
    if L == []:
        print(-1)
    else:
        print(max(L))
