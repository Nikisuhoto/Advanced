import os

dir_path = input()

data = {}

for file in os.listdir(dir_path):
    path = os.path.join(dir_path, file)
    if os.path.isfile(path):
        file_name, extension = file.split(".")
        if extension not in data:
            data[extension] = []
        data[extension].append(file)

for extension, file in sorted(data.items(), key=lambda kvp: kvp[0]):
    print(f'.{extension}')
    for file_name in sorted(file):
        print(f'- - - {file_name}')
