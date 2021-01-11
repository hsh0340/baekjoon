a,b,c = map(int,input().split())
numList = [a,b,c]
numList.remove(max(numList))
print(max(numList))
print(type(a))

