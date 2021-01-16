while True :
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a == 0 and b == 0 :
        break 
    elif b % a == 0:
        print("factor")
    elif a % b == 0 :
        print("multiple")
    else :
        print("neither")
    