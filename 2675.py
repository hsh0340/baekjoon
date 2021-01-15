case = int(input())

for i in range(case) :
    num, s = input().split()
    for j in range(len(s)) :
        print(s[j]*int(num),end='')
    print()


