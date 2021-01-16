n = int(input()) # 입력받을 케이스 개수

for i in range(n): # 케이스 개수만큼 반복
    count = 0 # 카운트 초기화
    a, b = input().split() 
    a = int(a)
    b = int(b) # 수 두개 입력받음
    for i in range(a,b+1) : # 두 수 범위만큼
        w = str(i) # 수를 문자열에 넣고
        count += w.count('0') # 그 수에 0 있으면 카운트 +1
    print(count)
