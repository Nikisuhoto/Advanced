n = int(input())
parking = set()

for _ in range(n):
    direction, car_number = input().split(', ')

    if direction == 'IN':
        parking.add(car_number)
    else:
        parking.remove(car_number)

if len(parking) == 0:
    print('Parking Lot is Empty')
else:
    print('\n'.join(parking))
    