T = input()
t = int(T)
for i in range(t):
    N = input()  # number of strings
    l = list(map(int, input().split()))
    sum = 0
    for i in range(len(l)-1):
        if l[i+1] > l[i]:
            sum = sum + abs(l[i+1]-l[i]-1)
        elif l[i+1] < l[i]:
            sum = sum + abs(l[i+1]-l[i]+1)
    print(sum)
