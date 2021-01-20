import sys

num = int(input())
numList = list(map(int,sys.stdin.readline().split()))


numList = list(set(numList))
numList = sorted(numList)
for i in range(len(numList)) :
    numList[i] = str(numList[i])
print(' '.join(numList))
