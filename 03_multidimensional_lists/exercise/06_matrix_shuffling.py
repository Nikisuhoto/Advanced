def is_valid_position(r1, c1, r2, c2, rows, cols):
    return 0 <= r1 < rows and 0 <= r2 < rows and 0 <= c1 < cols and 0 <= c2 < cols


r, c = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(r)]

while True:
    line = input()
    if line == 'END':
        break
    command = line.split()

    if command[0] != 'swap' or len(command) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if is_valid_position(row1, col1, row2, col2, r, c):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")
