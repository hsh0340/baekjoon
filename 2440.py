n = int(input())

for j in range(n):
    case = input()
    case = list(case)
    count = 0
    score = 0
    for i in range(len(case)):
        if case[i] == "O":
            count += 1
            score += count
        else :
            count = 0
    print(score)
                