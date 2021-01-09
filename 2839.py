n = int(input()) 
Box = 0 # 봉투 갯수
while True:
    if (n % 5) == 0: 
        Box = Box + (n//5) # 만약 15키로면 봉투에 3추가. 
        print(Box) 
        break
    n = n-3 # 설탕 에서 3 빼줌
    Box += 1 # 봉투에 1 추가. 다시 위로 올라감.
    if n < 0: 
        print("-1")
        break



