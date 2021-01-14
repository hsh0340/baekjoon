a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
sum = 0

numList = [a, b, c, d, e, f, g]
oddList = []
for i in range(len(numList)) :
    if numList[i] % 2 != 0 :
        sum += numList[i]
        oddList.append(numList[i])

if len(oddList) == 0 :
    print(-1)
else :
    print(sum)
    print(min(oddList))
