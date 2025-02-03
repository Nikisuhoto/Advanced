names = input().split(', ')
player1, player2 = names[0], names[1]
players_dictionary = {player1: 501, player2: 501}

matrix = []

for i in range(7):
    row = (list(input().split()))
    matrix.append(row)

counter = 0
trows = 0

while True:
    counter += 1

    trow = input()[1:-1].split(", ")
    trow_row = int(trow[0])
    trow_col = int(trow[1])

    if 7 <= trow_row >= 0 and 7 <= trow_col >= 0:
        if matrix[trow_row][trow_col].isdigit():
            if trows % 2 == 0:
                players_dictionary[player1] -= int(matrix[trow_row][trow_col])
                if players_dictionary[player1] <= 0:
                    print(player1)
        elif matrix[trow_row][trow_col] == "D":
            pass
        elif matrix[trow_row][trow_col] == "T":
            pass
        elif matrix[trow_row][trow_col] == "B":
            pass
    else:
        trows += 1
