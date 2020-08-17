T = input()
t = int(T)
for i in range(t):
    l = list(map(int, input().split()))
    power = int(l[1])
    health = int(l[0])
    while power > 0 and health > 0:
        health = health-power
        power = int(power/2)
        if health <= 0:
            print(1)
            break
        elif power <= 0:
            print(0)
            break
