T = input()
t = int(T)
for i in range(t):
    n = int(input())
    training_dict = {}
    sum_training = 0
    for j in range(n):
        l = list(map(str, input().split()))

        word = l[0]
        boolean = l[1]
        if word in training_dict:
            if boolean == '1':
                training_dict[word][1] += 1
            else:
                training_dict[word][0] += 1
        else:
            if boolean == '1':
                training_dict[word] = [0, 1]
            else:
                training_dict[word] = [1, 0]

    for key in training_dict:
        sum_training += max(training_dict[key])
    print(sum_training)
