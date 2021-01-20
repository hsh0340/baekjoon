a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] 
alpha = input() 
for i in a: # 크로아티아 문자에서
    alpha = alpha.replace(i, '*') # 입력받은 문자열에서 크로아티아 문자 있으면 별로 바꿈
print(len(alpha))

