n = int(input())

for i in range(n):
    scoreList = map(int,(input().split()))
    scoreList = list(scoreList)
    students = scoreList[0]
    del scoreList[0]
    scoreList = list(scoreList)
    average = sum(scoreList) / students
    count = 0
    for j in range(students) :
        if scoreList[j] > average :
            count += 1
    ratio = count / students * 100
    print("%0.3f" % ratio+"%") 