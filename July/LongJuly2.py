T = input()
t = int(T)
for i in range(t):
    N = input()  # number of rounds
    n = int(N)

    mortyPoints = 0
    chefPoints = 0
    for i in range(n):
        chefPower = 0
        mortyPower = 0
        l = list(map(int, input().split()))
        for digit in str(l[0]):
            chefPower = chefPower + int(digit)
        for digit in str(l[1]):
            mortyPower = mortyPower + int(digit)
        if chefPower > mortyPower:
            chefPoints = chefPoints+1
        elif mortyPower > chefPower:
            mortyPoints = mortyPoints+1
        elif mortyPower == chefPower:
            mortyPoints = mortyPoints+1
            chefPoints = chefPoints+1

    if chefPoints > mortyPoints:
        print(0, chefPoints)
    if mortyPoints > chefPoints:
        print(1, mortyPoints)
    if chefPoints == mortyPoints:
        print(2, chefPoints)
