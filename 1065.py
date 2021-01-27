n = int(input())

if n <= 99 :
    print(n)
else :
    count = 0
    for i in range(100, n+1) :
        n = list(str(i))
        if int(n[1]) - int(n[0]) == int(n[2]) - int(n[1]) :
            count += 1
    print(99 + count)

