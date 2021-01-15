s = list(input())

def makeBinary(num) :
    if num > 3 : # 100 101 110 111
        return ''.join([str((num//2)//2),str((num//2)%2),str(num%2)])
    else : # 000 001 010 011
        return ''.join(['0', str(num//2), str(num%2)])
        
result = []

for i in range(len(s)) :
    result.append(makeBinary(int(s[i])))
result = ''.join(result)

if result == '000' :
    print('0')
else :
    print(result.lstrip("0"))
    