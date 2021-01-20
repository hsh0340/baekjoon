date = int(input())
car1, car2, car3, car4, car5 = input().split()
cars = [car1, car2, car3, car4, car5]
count = 0

for i in range(len(cars)) :
    if int(cars[i]) == date :
        count += 1

print(count)
