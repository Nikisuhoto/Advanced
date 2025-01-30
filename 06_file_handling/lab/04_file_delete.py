import os

try:
    os.remove("example_new.txt")
    print("File deleted 🎈")
except FileNotFoundError:
    print("File is already deleted!")
