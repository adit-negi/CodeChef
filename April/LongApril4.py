import math as mt
T = input()
t = int(T)


def gcd(p, q):
    # Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1


for i in range(t):
    N = input()
    n = int(N)
    days = n//2
    print(days)
    primes = [1]
    non_primes = []
    for num in range(1, n + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    non_primes.append(num)
                    break
            else:
                primes.append(num)
    #print(len(primes), *primes)
    odd = n-days-1
    even_nprimes = []
    odd_nprimes = []
    for i in range(len(non_primes)):
        if non_primes[i] % 2 == 0:
            even_nprimes.append(non_primes[i])
        else:
            odd_nprimes.append(non_primes[i])

    for i in range(len(odd_nprimes)):

        for j in range(len(even_nprimes)):
            if is_coprime(odd_nprimes[i], even_nprimes[j]):
                print(2, even_nprimes[j], odd_nprimes[i])
                del even_nprimes[j]
                break
    for i in range(len(even_nprimes)):
        if is_coprime(primes[i+2], even_nprimes[i]):
            print(1, even_nprimes[i], primes[i+2])
