a, b, c, d, e = input().split()
numList = [a, b, c, d, e]
sum = 0
for i in range(len(numList)) :
    sum += int(numList[i]) * int(numList[i])
print(sum%10)