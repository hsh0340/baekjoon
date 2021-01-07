inputA = int(input())
inputB = int(input())

res1 = inputA * (inputB%10)
res2 = inputA * ((inputB//10)%10)
res3 = inputA * (inputB//100)
result = inputA * inputB

print(res1, res2, res3, result, sep='\n')