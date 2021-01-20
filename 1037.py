import sys

n = int(input())
numList = list(map(int,sys.stdin.readline().split()))

if len(numList) == 1 :
    print(numList[0] ** 2)
else :   
    print(max(numList) * min(numList))