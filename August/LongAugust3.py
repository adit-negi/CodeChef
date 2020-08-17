import math
T = input()
t = int(T)
for i in range(t):
    l = list(map(int, input().split()))
    Pr = int(l[1])
    Pc = int(l[0])
    chef_integers = math.ceil(Pc/9)
    morty_integers = math.ceil(Pr/9)
    if chef_integers < morty_integers:
        print(0, chef_integers)
    elif chef_integers >= morty_integers:
        print(1, morty_integers)
