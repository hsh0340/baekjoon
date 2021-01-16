minguk = list(input().split())
mansae = list(input().split())
mingukSum = 0
mansaeSum = 0
for i in range(len(minguk)) :
    mingukSum += int(minguk[i])
    mansaeSum += int(mansae[i])
if mingukSum > mansaeSum or mingukSum == mansaeSum :
    print(mingukSum)
else :
    print(mansaeSum)
