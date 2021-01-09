a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
sum = 0
scoreArr = [a,b,c,d,e]
for i in range(len(scoreArr)) :
    if scoreArr[i] < 40 :
        scoreArr[i] = 40
    sum = sum + scoreArr[i]
print(sum//5)