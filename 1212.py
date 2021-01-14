def makeBinary(num) :
    if num > 3 : # 100 101 110 111
        return (num//2)//2,(num//2)%2,num%2
    elif num == 1 : # 001
        return '001'
    else : # 000 010 011
        return ((0, num//2, num%2))
        
s 
s = list(input())
result = []

for i in range(len(s)) :
    result = ''.join(str(makeBinary(s[i])))

print(result)