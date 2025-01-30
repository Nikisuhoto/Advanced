n = 6
matrix = []

for i in range(n):
    row = (list(input().split()))
    matrix.append(row)

position = input().strip()[1:-1].split(", ")
position_row = int(position[0])
position_col = int(position[1])

while True:
    command = input().split(", ")
    if command[0] == 'Stop':
        break

    directions = {
        "left": lambda r, c: (r, c - 1),
        "right": lambda r, c: (r, c + 1),
        "up": lambda r, c: (r - 1, c),
        "down": lambda r, c: (r + 1, c)
    }

    position_row, position_col = directions[command[1]](position_row, position_col)

    if command[0] == 'Create':
        if matrix[position_row][position_col] == ".":
            matrix[position_row][position_col] = command[2]
        else:
            continue

    if command[0] == 'Update':
        if matrix[position_row][position_col].isdigit() or matrix[position_row][position_col].isalpha():
            matrix[position_row][position_col] = command[2]
        else:
            continue

    if command[0] == 'Delete':
        if matrix[position_row][position_col].isdigit() or matrix[position_row][position_col].isalpha():
            matrix[position_row][position_col] = "."
        else:
            continue
    if command[0] == 'Read':
        if matrix[position_row][position_col].isdigit() or matrix[position_row][position_col].isalpha():
            print(matrix[position_row][position_col])

for row in matrix:
    print(*row, end="\n")
