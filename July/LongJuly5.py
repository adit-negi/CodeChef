from collections import Counter
T = input()
t = int(T)
for i in range(t):
    N = input()  # number of strings
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    L = []
    flag = 0
    count = 0
    need = 0
    minimmums = []
    C = []
    C.extend(A)
    C.extend(B)
    if flag == 0:
        n = int(N)
        C = list(dict.fromkeys(C))
        A1 = dict(Counter(A))
        B1 = dict(Counter(B))
        for i in range(len(C)):
            if C[i] in A1.keys():
                a = A1[C[i]]
            else:
                a = 0
            if C[i] in B1.keys():
                b = B1[C[i]]
            else:
                b = 0
            need = (a-b)/2
            Need = abs(need)
            if (int(need*2)) % 2 != 0:
                flag = 1
                break
            if (int(Need) == 0):
                pass
            else:
                a = [C[i]]*int(Need)
                L.extend(a)
        L.sort()
        abs_min = min(C)
        for i in range(int(len(L)/2)):
            count = count + min(L[i], 2*abs_min)
    if flag == 0:
        print(count)
    else:
        print(-1)
