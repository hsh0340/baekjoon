s = list(input())
result = []
for i in range(len(s)) :
    if 64 < ord(s[i]) < 91 :
        result.append(s[i])

print(''.join(result))