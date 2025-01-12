numbs = tuple([float(el) for el in input().split()])

data = {}

for el in numbs:
    data[el] = numbs.count(el)

for key, value in data.items():
    print(f'{key:.1f} - {value} times')