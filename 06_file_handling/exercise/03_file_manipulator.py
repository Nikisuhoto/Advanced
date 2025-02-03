import os

command = input()

while command != "End":
    data = command.split("-")
    file_name = data[1]

    if command.startswith("Create"):
        if os.path.exists(file_name):
            with open(file_name, 'a') as file:
                file.truncate(0)
        else:
            with open(file_name, "w") as fp:
                pass
    elif command.startswith("Add"):
        content = data[2] + "\n"
        with open(file_name, "a") as file:
            file.write(content)

    elif command.startswith("Replace"):
        old_str = data[2]
        new_str = data[3]
        try:
            with open(file_name, "r") as file:
                content = file.read()
            with open(file_name, "w") as file:
                file.write(content)
        except FileNotFoundError:
            print("An error occurred")
    elif command.startswith("Delete"):
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")

    command = input()