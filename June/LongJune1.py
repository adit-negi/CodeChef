T = input()
t = int(T)

for i in range(t):
    Nk = list(map(int, input().split()))
    Prices = list(map(int, input().split()))
    N = Nk[0]
    k = Nk[1]
    loss = 0
    for i in range(N):
        if Prices[i] > k:
            loss = loss + Prices[i] - k
    print(loss)
