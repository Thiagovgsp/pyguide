carlist = []

while True:
    cars = input('Enter: ')
    if cars == '':
        break

    carlist.append(cars)
carlist.sort()
print(carlist)