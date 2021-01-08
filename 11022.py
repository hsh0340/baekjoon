t = int(input())
for i in range(t):
    a, b = input().split()
    print('Case #%s: %s + %s = %s'%(i+1, int(a), int(b), int(a)+int(b)))