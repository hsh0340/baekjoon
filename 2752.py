num = input().split()
for i in range(len(num)) :
    num[i] = int(num[i])
num.sort()
for i in range(len(num)) :
    num[i] = str(num[i])
print(' '.join(num))
