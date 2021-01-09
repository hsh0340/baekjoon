n = int(input()) # 입력받을 갯수
scoreList = list(map(int,input().split())) # 정수 여러개 입력받아서 리스트에 넣음
maxScore = max(scoreList) # 제일 높은 점수

for i in range(n):
    scoreList[i] = scoreList[i] / maxScore * 100 # 리스트 안에 점수 바꿔치기
    average = sum(scoreList) / n
print(average)
