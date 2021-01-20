import sys
numList = list(map(int,sys.stdin.readline().split()))
# print(numList[0] ** numList[1] % numList[2])
print(pow(numList[0],numList[1],numList[2]))