s = input()
s = list(s) 

newList = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,]

for i in range(len(s)):
    newList[ord(s[i]) - 97] = i 
    if s.count(s[i]) > chr(1) :
        s.insert(i,5)
        #s.index(i) = "A"
print(s)
    