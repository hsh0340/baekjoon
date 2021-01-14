a, b = input().split()
a = int(a)
b = int(b)

aDivisor =[]
bDivisor = []
result = []

for i in range(1,a+1) :
    if a % i == 0 :
        aDivisor.append(str(i))
for i in range(1,b+1) :
    if b % i == 0 :
        bDivisor.append(str(i))

for s1 in aDivisor:
    for s2 in bDivisor:
        if s1 == s2:
            result.append(s1)

result = list(map(int, result))

max = max(result)
min = a//max * b//max * max
print(max)
print(min)
