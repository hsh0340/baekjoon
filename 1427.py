num_list = list(map(int, input())) # 리스트 입력받음
num_list.sort(reverse=True) # 내림차순 정렬
for i in num_list: # 문자열로 바꿈
    print(i, end='')