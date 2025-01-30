n = int(input())
matrix = []
player = []
coins_collected = 0
walls = []

for row in range(n):
    matrix.append(list(input().split()))
    for col in range(n):
        if matrix[row][col] == "P":
            player.append([row, col])
        if matrix[row][col] == "X":
            walls.append([row, col])

moves = {
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}

player_row = player[0][0]
player_col = player[0][1]
matrix[player_row][player_col] = "0"

while True:
    command = input().strip()
    if command not in ("up", "down", "left", "right"):
        continue

    new_player_row, new_player_col = moves[command](player_row, player_col)

    if new_player_row < 0:
        new_player_row = n - 1
    if new_player_row >= n:
        new_player_row = 0
    if new_player_col < 0:
        new_player_col = n - 1
    if new_player_col >= n:
        new_player_col = 0

    player.append([new_player_row, new_player_col])
    if matrix[new_player_row][new_player_col] == "X":
        print(f"Game over! You've collected {int(coins_collected / 2)} coins.")
        break

    else:
        map(int, matrix[new_player_row][new_player_col])
        coins_collected += int(matrix[new_player_row][new_player_col])
        matrix[new_player_row][new_player_col] = "0"

    player_row, player_col = new_player_row, new_player_col

    if coins_collected > 100:
        print(f"You won! You've collected {coins_collected} coins.")
        break

print("Your path:")
for loc in player:
    print(loc)
