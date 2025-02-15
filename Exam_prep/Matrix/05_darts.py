names = input().split(', ')
player1, player2 = names[0], names[1]
players_dictionary = {player1: 501, player2: 501}

matrix = []

for i in range(7):
    row = (list(input().split()))
    matrix.append(row)

trows = 0

while True:

    trow = input()[1:-1].split(", ")
    trow_row = int(trow[0])
    trow_col = int(trow[1])
    current_row_sum = 0
    current_col_sum = 0
    current_row_col_sum = 0

    if 7 >= trow_row >= 0 and 7 >= trow_col >= 0:
        if matrix[trow_row][trow_col].isdigit():
            if trows % 2 == 0:
                players_dictionary[player1] -= int(matrix[trow_row][trow_col])
                if players_dictionary[player1] <= 0:
                    result = player1
                    break
            else:
                players_dictionary[player2] -= int(matrix[trow_row][trow_col])
                if players_dictionary[player2] <= 0:
                    result = player2
                    break
        elif matrix[trow_row][trow_col] == "D":
            for r in matrix[trow_row]:
                if r.isdigit():
                    current_row_sum += int(r)
            for r in matrix:
                if r[trow_col].isdigit():
                    current_col_sum += int(r[trow_col])
            current_row_col_sum = (current_row_sum + current_col_sum) * 2

        elif matrix[trow_row][trow_col] == "T":
            for r in matrix[trow_row]:
                if r.isdigit():
                    current_row_sum += int(r)
            for r in matrix:
                if r[trow_col].isdigit():
                    current_col_sum += int(r[trow_col])

            current_row_col_sum = (current_row_sum + current_col_sum) * 3

        elif matrix[trow_row][trow_col] == "B":
            if trows % 2 == 0:
                players_dictionary[player1] = 0
            else:
                players_dictionary[player2] = 0

        if trows % 2 == 0:
            players_dictionary[player1] -= current_row_col_sum
        else:
            players_dictionary[player2] -= current_row_col_sum

    if players_dictionary[player1] <= 0:
        result = player1
        break
    if players_dictionary[player2] <= 0:
        result = player2
        break
    else:
        trows += 1

print(f'{result} won the game with {(trows // 2) + 1} throws!')
