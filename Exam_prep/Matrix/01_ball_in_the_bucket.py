rows = 6
cols = 6
board = []

for i in range(rows):
    row = input().split()
    board.append(row)

throws = []
for _ in range(3):
    throw = input().strip()[1:-1].split(", ")
    throws.append((int(throw[0]), int(throw[1])))

score = 0
visited_buckets = set()

for row, col in throws:
    if 0 <= row < 6 and 0 <= col < 6:
        if board[row][col] == "B" and (row, col) not in visited_buckets:
            visited_buckets.add((row, col))

            for i in range(6):
                if board[i][col].isdigit():
                    score += int(board[i][col])

            # score += sum(int(board[i][col]) for i in range(6))

if score >= 100:
    if score < 200:
        price = "Football"
    elif score < 300:
        price = "Teddy Bear"
    else:
        price = "Lego Construction Set"

    print(f"Good job! You scored {score} points, and you've won {price}.")

else:
    points_needed = 100 - score
    print(f"Sorry! You need {points_needed} points more to win a prize.")
