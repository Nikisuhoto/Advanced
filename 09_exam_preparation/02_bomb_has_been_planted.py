rows, cols = map(int, input().split(", "))
matrix = []

terrorists_position = []
bomb_position = []
counter_terrorist = []
seconds = 16
time_needed = 0
defusing_over = 0
stay_on_bomb = False
is_bomb_defusing = False
boom = False
terrorists_kill = False
bomb_not_successful = False

for row in range(rows):
    r = list(input())
    matrix.append(list(r))

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "T":
            terrorists_position.append([row, col])
        elif matrix[row][col] == "B":
            bomb_position.append([row, col])
        elif matrix[row][col] == "C":
            counter_terrorist.append([row, col])

player_row, player_col = counter_terrorist[0][0], counter_terrorist[0][1]

while True:

    moves = {
        "left": lambda r, c: (r, c - 1),
        "right": lambda r, c: (r, c + 1),
        "up": lambda r, c: (r - 1, c),
        "down": lambda r, c: (r + 1, c),
        "defuse": lambda r, c: (r, c)
    }

    command = input().strip()
    if command not in ("up", "down", "left", "right", "defuse"):
        seconds -= 1
        if seconds < 0:
            boom = True
            break
        continue

    player_row, player_col = moves[command](player_row, player_col)

    if player_row < 0:
        player_row = 0
    if player_row >= rows:
        player_row = rows - 1
    if player_col < 0:
        player_col = 0
    if player_col >= cols:
        player_col = cols - 1

    if command == "defuse":

        if matrix[player_row][player_col] == "B":
            stay_on_bomb = True
        if stay_on_bomb:

            seconds -= 4
            if seconds < 0:
                boom = True
                bomb_not_successful = True
                time_needed = seconds * (-1)

                break

            else:
                matrix[player_row][player_col] = "D"
                defusing_over = seconds
                is_bomb_defusing = True
                break
        seconds -= 2
        if seconds < 0:
            boom = True
            bomb_not_successful = True
            time_needed = seconds * -1

            seconds += 1
            break

    if matrix[player_row][player_col] == "T":
        matrix[player_row][player_col] = "*"
        terrorists_kill = True
        break

    seconds -= 1
    if seconds < 0:
        boom = True
        break

if boom:
    r, c = bomb_position[0][0], bomb_position[0][1]
    matrix[r][c] = "X"
if terrorists_kill:
    pass

if not boom and not bomb_not_successful and not terrorists_kill:
    print("Counter-terrorist wins!")

if boom or terrorists_kill or bomb_not_successful:
    print("Terrorists win!")

if bomb_not_successful:
    print("Bomb was not defused successfully!")
    print(f"Time needed: {time_needed} second/s.")

if is_bomb_defusing:
    print(f"Bomb has been defused: {defusing_over + 1} second/s remaining.")

for row in range(rows):
    if row > 0:
        print("")
    for col in range(cols):
        print(matrix[row][col], end="")
