import sys

case = int(input())
for i in range(case) :
    numList = list(map(int,sys.stdin.readline().split()))
    for j in range(2) :
        numList.remove(max(numList))
    print(max(numList))
