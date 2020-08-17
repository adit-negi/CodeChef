T = input()
t = int(T)
for i in range(t):
    TS = input()
    a, Ts = int(TS), int(TS)
    JS, count = 0,0
    while (Ts != 1):
        if (Ts % 2 != 0):
            break
        Ts = Ts // 2
        count = count+1
    x = pow(2, count+1)
    JS = a // x
    print(JS)
