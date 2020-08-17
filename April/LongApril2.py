T = input()
t = int(T)
j = 0

for i in range(t):
    N = int(input())
    P = list(map(int, input().split()))
    P.sort(reverse=True)
    profit = 0
    for j in range(N):
        #k = j+1
        if P[j] > j:
            profit = profit + (P[j]-j)
        '''if k < N:
            for a in range(k, N):
                if P[a] > 0:
                    P[a] = P[a]-1'''

    print(profit % 1000000007)
