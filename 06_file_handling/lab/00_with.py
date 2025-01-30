with open("file.txt", "w") as new_file:
    new_file.write("Hello World!!!")
    print(new_file.closed)
print(new_file.closed)