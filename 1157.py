s = input()
s = s.upper()

numList = [0] * 26
asci = 65

for i in range(len(s)) :
    numList[ord(s[i])-65] += 1
maxIndex = numList.index(max(numList))

if numList.count(max(numList)) > 1 :
    print("?")
else :
    print(chr(maxIndex+65))
