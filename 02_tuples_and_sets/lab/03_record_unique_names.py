n = int(input())
names = []
for _ in range(n):
    name = input()
    names.append(name)

result = set(names)
for name in result:
    print(name)