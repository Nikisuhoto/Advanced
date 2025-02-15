n = int(input())

matrix = []
pacman_position = 0
stars_count = 0
ghosts_count = 0
freezers_count = 0
health = 100
immunity = False

for i in range(n):
    row = list(input().strip())
    matrix.append(row)
    if "P" in row:
        pacman_position = (i, row.index("P"))
    stars_count += row.count("*")
    ghosts_count += row.count("G")
    freezers_count += row.count("F")

directions = {
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}

while True:
    command = input()
    if command == "end":
        break

    new_row, new_col = directions[command](pacman_position[0], pacman_position[-1])

    if new_row < 0:
        new_row = n - 1
    if new_row == n:
        new_row = 0
    if new_col < 0:
        new_col = n - 1
    if new_col == n:
        new_col = 0

    matrix[pacman_position[0]][pacman_position[1]] = "-"
    pacman_position = (new_row, new_col)

    if matrix[new_row][new_col] == "*":
        stars_count -= 1
        matrix[new_row][new_col] = "-"

    if matrix[new_row][new_col] == "G":
        if not immunity:
            health -= 50
            if health <= 0:
                health = 0
                break
        else:
            immunity = False
        matrix[new_row][new_col] = "-"

    if matrix[new_row][new_col] == "F":
        immunity = True
        matrix[new_row][new_col] = "-"

    if stars_count == 0:
        break

if health == 0:
    print(f"Game over! Pacman last coordinates [{pacman_position[0]},{pacman_position[1]}]")

elif stars_count == 0:
    print("Pacman wins! All the stars are collected.")

else:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")

if stars_count > 0:
    print(f"Uncollected stars: {stars_count}")

matrix[pacman_position[0]][pacman_position[1]] = "P"

for row in matrix:
    print(''.join(row))
