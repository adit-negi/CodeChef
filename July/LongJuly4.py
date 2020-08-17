T = input()
t = int(T)
for i in range(t):
    N = input()  # number of rounds
    n = int(N)
    list_of_vertices = []
    list_of_x = []
    list_of_y = []
    xcoordinte = 0
    ycoordinte = 0
    for i in range(4*n-1):
        l = list(map(int, input().split()))
        list_of_vertices.append(l)
        list_of_x.append(l[0])
        list_of_y.append(l[1])
    for element in list_of_x:
        xcoordinte = xcoordinte ^ element
    for element in list_of_y:
        ycoordinte = ycoordinte ^ element
    print(xcoordinte, ycoordinte)
