import os.path

file_path = os.path.join("files", "numbers.txt")
file = open(file_path)

content = file.read().split("\n")

numbers = []
for line in content:
    try:
        el = int(line)
        numbers.append(el)
    except ValueError:
        continue

print(sum(numbers))


