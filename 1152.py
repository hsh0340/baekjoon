sen = input()
if sen == " " :
    print(0)
else:
    sen = sen.strip()
    print((sen.count(' '))+1)