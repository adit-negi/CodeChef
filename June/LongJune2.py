T = input()
t = int(T)

for i in range(t):
    line = input()
    total_kids = len(line)
    max_pairs = 0
    i = 0
    temp = ''
    while i < total_kids-1:

        if line[i] == 'x' and line[i+1] == 'y':
            max_pairs = max_pairs+1
            i = i+2
        elif line[i] == 'y' and line[i+1] == 'x':
            max_pairs = max_pairs+1
            i = i+2
        else:
            i = i+1

    print(max_pairs)
