# from collections import deque
#
# elves_energy = deque(map(int, input().split()))
# present_parts = list(map(int, input().split()))
# toys = 0
# total_energy = 0
# counter = 1
#
# while elves_energy and present_parts:
#
#     current_elves_energy = elves_energy[0]
#     current_present_parts = present_parts[-1]
#     current_current_present_parts = 0
#
#     if current_elves_energy < 5:
#         elves_energy.popleft()
#         current_elves_energy = elves_energy[0]
#         current_present_parts = present_parts[-1]
#
#     if counter % 3 == 0 and counter >= 3:
#         current_current_present_parts = current_present_parts * 2
#         if current_elves_energy >= current_current_present_parts:
#             toys += 2
#             current_elves_energy += 1  # cookie case
#             total_energy += current_current_present_parts
#             present_parts.pop()
#             elves_energy.rotate(-1)
#             elves_energy.pop()
#             elves_energy.append(current_elves_energy)
#
#     if counter % 5 == 0 and current_elves_energy >= current_present_parts and counter >= 5:
#         if counter % 3 == 0 and counter >= 3:
#             current_current_present_parts = current_present_parts * 2
#             if current_elves_energy >= current_current_present_parts:
#                 toys += 2
#                 current_elves_energy += 1  # cookie case
#                 total_energy += current_current_present_parts
#                 present_parts.pop()
#                 elves_energy.rotate(-1)
#                 elves_energy.pop()
#                 elves_energy.append(current_elves_energy)
#
#     if current_elves_energy >= current_present_parts:
#         toys += 1
#         current_elves_energy += 1  # cookie case
#         total_energy += current_present_parts
#         present_parts.pop()
#         elves_energy.rotate(-1)
#         elves_energy.pop()
#         elves_energy.append(current_elves_energy)
#
#     else:
#         current_elves_energy *= 2
#         elves_energy.rotate(-1)
#         elves_energy.pop()
#         elves_energy.append(current_elves_energy)
#
#     counter += 1
#
# print(toys)
# print(total_energy)
# print(*elves_energy)

from collections import deque

elves_energy = deque(map(int, input().split()))
present_parts = list(map(int, input().split()))

toys = 0
total_energy = 0
counter = 0

while elves_energy and present_parts:
    current_elves_energy = elves_energy.popleft()

    if current_elves_energy < 5:
        continue

    current_present_parts = present_parts.pop()
    counter += 1

    if counter % 3 == 0:
        needed_energy = current_present_parts * 2
    else:
        needed_energy = current_present_parts

    if counter % 5 == 0:
        if current_elves_energy >= needed_energy:
            total_energy += needed_energy
            current_elves_energy -= needed_energy

        else:
            present_parts.append(current_present_parts)
            current_elves_energy *= 2
            elves_energy.append(current_elves_energy)
            continue
    else:
        if current_elves_energy >= needed_energy:
            total_energy += needed_energy
            current_elves_energy -= needed_energy
            toys += 2 if counter % 3 == 0 else 1
            current_elves_energy += 1
        else:
            present_parts.append(current_present_parts)
            current_elves_energy *= 2
            elves_energy.append(current_elves_energy)
            continue

    elves_energy.append(current_elves_energy)

print(f"Toys: {toys}")
print(f"Energy: {total_energy}")
if elves_energy:
    print(f"Elves left: {', '.join(map(str, elves_energy))}")
if present_parts:
    print(f"Boxes left: {', '.join(map(str, present_parts))}")
