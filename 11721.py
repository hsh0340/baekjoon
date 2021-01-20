a = input() # 입력받은 문자열
 
for i in range(0,len(a),10): # 0부터 문자열의 길이까지, 10씩 증가
    print(a[i:i+10]) # 문자열 a의 i부터 i+10 까지 출력