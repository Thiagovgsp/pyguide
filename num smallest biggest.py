smallest = None
biggest = None

while True:
    number = input('enter a num: ')
    if number == 'done':
        break

    try:
        val = int(number)

        try:
            if biggest < val:
                biggest = val

            if smallest > val:
                smallest = val

            
        except:
            biggest = val
            smallest = val
            continue

    except:
        print('try again')
        continue


print('max', biggest)
print('min', smallest)

