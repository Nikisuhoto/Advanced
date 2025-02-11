n = int(input())
ship = [0, 0]
matrix = []

for r in range(n):
    matrix.append(input().split())
    for c in range(n):
        if matrix[r][c] == "S":
            ship = [r, c]
            matrix[r][c] = "."
            break

resources = 100

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    if resources < 5:
        print("Mission failed! The spaceship was stranded in space.")
        break

    resources -= 5
    command = input()
    move = moves[command]
    new_r = ship[0] + move[0]
    new_c = ship[1] + move[1]

    if 0 <= new_r < n and 0 <= new_c < n:
        ship = [new_r, new_c]
        if matrix[new_r][new_c] == "R":
            resources += 10
            if resources > 100:
                resources = 100
        elif matrix[new_r][new_c] == "M":
            resources -= 5
            matrix[new_r][new_c] = "."
        elif matrix[new_r][new_c] == "P":
            print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
            break

    else:
        print("Mission failed! The spaceship was lost in space.")
        break

if matrix[ship[0]][ship[1]] not in "PR":
    matrix[ship[0]][ship[1]] = "S"

for row in matrix:
    print(*row)
