
T = input()
t = int(T)
for i in range(t):
    s = str(input())
    p = str(input())
    s = ''.join(sorted(s))
    dictS = {}
    dicts = {}
    outputstr = ""
    # Initializing dictionary
    for i in range(len(s)):
        if s[i] in dictS:
            dictS[s[i]] = dictS[s[i]] + 1
        else:
            dictS[s[i]] = 1
    flag = 0
    # Initializing dictionary 2
    for i in range(len(s)):
        if s[i] in dicts:
            dicts[s[i]] = dicts[s[i]] + 1
        else:
            dicts[s[i]] = 1
    # removibg substring
    for i in range(len(p)):
        if p[i] in dictS:
            dictS[p[i]] -= 1
    index = 0
    small = p[0]
    for i in range(len(p)):
        if p[i] < small:
            small = p[i]

    for key in dictS:
        if key <= small:

            outputstr += dictS[key]*key
            dictS[key] = 0
            index = index + dicts[key]

    for key in dictS:
        if key < p[0] and key > small:
            outputstr += key*dictS[key]
            index = index+dicts[key]
            dictS[key] = 0

        elif key == p[0]:
            for i in range(0, len(p)):
                if p[i] < s[index]:

                    flag = 1
                    outputstr += p
                    print(outputstr)
                    break
                if p[i] > s[index]:
                    outputstr += s[index]*dictS[s[index]]
                    dictS[s[index]] = 0
                    break
                else:
                    continue
                index = index+1
        elif key > p[0]:
            if flag == 0:
                outputstr += p
            flag = 1
            break
    for key in dictS:
        outputstr += dictS[key]*key
    if flag == 0:
        outputstr += p
    print(outputstr)
