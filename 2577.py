a = int(input())
b = int(input())
c = int(input())
abcList = list(str(a*b*c))

for i in range(10):
    print(abcList.count(str(i)))