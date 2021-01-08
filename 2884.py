h, m = input().split()
h = int(h)
m = int(m)

if m >= 45:
    print(h, m-45)
elif m < 45:
    m = 15 + m
    if h == 0:
        print(23, m)
    else :
        print(h-1, m)