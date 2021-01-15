n = int(input())
numList = []
for i in range(n):
    numList.append(int(input()))

for i in range(len(numList)) :
    print(min(numList))
    numList.remove(min(numList))
