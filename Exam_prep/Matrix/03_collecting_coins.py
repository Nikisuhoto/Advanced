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

while True:
    command = input()
    new_player_row, new_player_col = moves[command](player_row, player_col)
    player.append([new_player_row, new_player_col])
    if new_player_row < 0 or new_player_row >= n or new_player_col < 0 or new_player_col >= n:
        exit()

for i in range(len(matrix)):
    print(matrix[i])

print(player)
print(walls)