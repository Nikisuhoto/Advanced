from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

points = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
presents = {}

while materials and magic:
    total_magic = materials[-1] * magic[0]
    if total_magic in points:
        new_present = points[total_magic]
        if new_present not in presents:
            presents[new_present] = 0
        presents[new_present] += 1
        materials.pop()
        magic.popleft()
    elif total_magic < 0:
        materials.append(materials.pop() + magic.popleft())
    elif total_magic > 0:
        magic.popleft()
        materials[-1] += 15
    else:
        if materials[-1] == 0:
            materials.pop()
        if magic[0] == 0:
            magic.popleft()

if ("Doll" in presents and "Wood train" in presents) or (
        "Teddy bear" in presents and "Bicycle" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for key, value in sorted(presents.items()):
    print(f"{key}: {value}")
