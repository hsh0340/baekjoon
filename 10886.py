n = int(input())
teamMember = []

for i in range(n) :
    teamMember.append(int(input()))

cute = teamMember.count(1)
notCute = teamMember.count(0)

if cute > notCute :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")
    