import math as mt
T = input()
t = int(T)
for i in range(t):
    P = list(map(int, input().split()))
    n = P[0]
    k = P[1]
    a = list()

    # insert all 2's in list
    while n % 2 == 0:
        a.append(2)
        n = n // 2

    # n must be odd at this point
    # so we skip one element(i=i+2)
    for i in range(3, mt.ceil(mt.sqrt(n)), 2):
        while n % i == 0:
            n = n / i
            a.append(i)

    # This is to handle when n>2 and
    # n is prime
    if n > 2:
        a.append(n)

    # if size(a)<k,k factors are not possible
    if len(a) < k:
        print("0")
    else:
        print("1")
    '''chkthis = 2
    while len(primes) < K:
        ptest = [chkthis for i in primes if chkthis % i == 0]
        primes += [] if ptest else [chkthis]
        chkthis += 1
    minimum = 1
    for i in range(K):
        minimum = minimum*primes[i]
    count = 0
    for i in range(1, minimum+1):
        if minimum % i == 0:
            count = count+1
    if count > X:
        print(0)
    else:
        print(1)'''
