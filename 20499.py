s = input()
s = s.split('/')
if (int(s[0]) + int(s[2])) < int(s[1]) or s[1] == '0' :
    print("hasu")
else :
    print("gosu")