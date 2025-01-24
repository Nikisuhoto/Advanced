from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

rotate = False
gift = {}
present_try = 0

while materials and magic:

    if rotate == False:
        present_try = materials[-1] + magic[0]
    if 100 <= present_try <= 199:
        if 'Gemstone' not in gift.keys():
            gift['Gemstone'] = 0
        gift["Gemstone"] += 1
        materials.pop(-1)
        magic.popleft()
        rotate = False
        continue

    elif 200 <= present_try <= 299:
        if 'Porcelain Sculpture' not in gift.keys():
            gift['Porcelain Sculpture'] = 0
        gift["Porcelain Sculpture"] += 1
        materials.pop(-1)
        magic.popleft()
        rotate = False
        continue

    elif 300 <= present_try <= 399:
        if 'Gold' not in gift.keys():
            gift['Gold'] = 0
        gift["Gold"] += 1
        materials.pop(-1)
        magic.popleft()
        rotate = False
        continue

    elif 400 <= present_try <= 499:
        if 'Diamond Jewellery' not in gift.keys():
            gift['Diamond Jewellery'] = 0
        gift["Gold"] += 1
        materials.pop(-1)
        magic.popleft()
        rotate = False
        continue

    elif rotate == True:
        materials.pop(-1)
        magic.popleft()
        rotate = False
        continue

    else:
        if present_try < 100:
            if present_try % 2 == 0:
                present_try = materials[-1] * 2 + magic[0] * 3

            elif present_try % 2 != 0:
                present_try *= 2

        elif present_try > 499:
            present_try /= 2

    rotate = True

if "Gemstone" in gift.keys() and "Porcelain Sculpture" in gift.keys() or "Gold" in gift.keys() and "Diamond Jewellery" in gift.keys():
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if magic:
    magic = list(magic)
    print(f"Magic left: {', '.join(map(str, magic))}")
if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if gift:
    for key, value in gift.items():
        print(f"{key}: {value}")