n = int(input())

matrix = []
alice = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            matrix[row][col] = "*"
            alice = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
tea_bags = 0

while tea_bags < 10:

    direction = input()
    move = possible_moves[direction]
    row = alice[0] + move[0]
    col = alice[1] + move[1]

    if row < 0 or row >= n or col < 0 or col >= n:
        break

    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break
    if matrix[row][col] not in ".*":
        tea_bags += int(matrix[row][col])
    matrix[row][col] = "*"
    alice = [row, col]

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(*row) for row in matrix]