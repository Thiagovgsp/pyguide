list = []
find5 = None
indice5 = []

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break

    try:
        fnum = int(number)
        list.append(fnum)

    except ValueError:
        print('type a number')
        continue

count5 = list.count(5)

if 5 in list:
    find5 = list.index(5)
    indice5 = [index + 1 for index, value in enumerate(list) if value == 5]

if find5 is not None and count5 > 1:
    print(f'The number of 5 is {count5} and appears in this position {indice5}')
else:
    print('no five')