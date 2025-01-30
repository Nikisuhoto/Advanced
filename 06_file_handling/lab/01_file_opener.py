# file = open("example.txt")
# print(file.read())

try:
    file = open("text.txt")
    print('File found')
except FileNotFoundError:
    print("File not found")
