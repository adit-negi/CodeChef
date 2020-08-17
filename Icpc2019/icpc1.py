t = int(input())
for i in range(t):
    integer = int(input())
    str_integer = str(integer)
    minimum = int(str_integer[1:])

    for i in range(len(str_integer)):
        if i+1 < len(str_integer):
            temp_int = int(str_integer[:i] + str_integer[i+1:])
        else:
            temp_int = int(str_integer[:i])
        if temp_int < minimum:
            minimum = temp_int
    print(minimum)
