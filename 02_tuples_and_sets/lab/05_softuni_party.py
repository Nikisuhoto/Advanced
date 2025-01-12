n = int(input())

reservations = set()

for _ in range(n):
    reservation = input()
    reservations.add(reservation)

guest_reservation = input()
while guest_reservation != 'END':
    reservations.remove(guest_reservation)
    guest_reservation = input()

print(len(reservations))
for guest in sorted(reservations):
    print(guest)