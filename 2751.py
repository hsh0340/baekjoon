import sys

case = int(input())
numList = []

for i in range(case) :
    numList.append(int(sys.stdin.readline()))

numListLength = len(numList)
numList = sorted(numList)

for i in range(numListLength) :
    print(numList[i])

