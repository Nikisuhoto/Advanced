chars_to_replace = ["-", ",", ".", "!", "?"]
with open("exercise_files/text.txt") as file:
    text = file.readlines()

for index in range(0, len(text), 2):

    for char in chars_to_replace:
        text[index] = text[index].replace(char, "@")

    current_line = text[index].split()
    for w_index in range(len(current_line)-1, -1, -1):
        print(current_line[w_index], end=" ")
    print()