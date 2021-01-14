s = input()
newList = []

for j in range(97,123): # 아스키코드 소문자 범위
    if s.find(chr(j)) != -1 : # 아스키코드가 문자열에 포함되어있을 때
        newList.append(s.index(chr(j))) # 문자의 위치를 리스트에 추가.
    else :
        newList.append(s.find(chr(j))) # -1을 리스트에 추가

result = list(map(str, newList))
print(' '.join(result))
#1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
