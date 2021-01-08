n = int(input())
arr = input()
newList = list(arr)
result = 0
for i in range(len(newList)) :
    result += int(newList[i])
print(result)
