file = open("example_new.txt", "w")

file.write("Hello again from new file!\n")

file = open("example_new.txt")
print(file.read())

print(file.closed)
file.close()
print(file.closed)

