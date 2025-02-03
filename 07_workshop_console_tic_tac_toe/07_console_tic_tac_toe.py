class InvalidPositionNumber(Exception):
    pass


class PositionTaken(Exception):
    pass


def obtain_valid_position(player_name, matrix):
    while True:
        try:
            selected_position = int(input(f'{player_name}, please select a spot: '))
            if selected_position < 1 or selected_position > 9:
                raise InvalidPositionNumber
            row, col = position_mapper[selected_position]
            if matrix[row][col] != ' ':
                raise PositionTaken
            return selected_position

        except ValueError:
            print("Please enter a valid number")
        except InvalidPositionNumber:
            print("Please enter a number between 1-9")
        except PositionTaken:
            print("Please select an empty position")


def print_board(matrix):
    for row in matrix:
        print(f'|  {"  |  ".join(row)}  |')


def is_winner(player_symbol, matrix):
    # row winner
    for row in matrix:
        if all([el == player_symbol for el in row]):
            return True
    # col winner
    for col_index in range(len(matrix)):
        if all([matrix[row_index][col_index] == player_symbol for row_index in range(len(matrix))]):
            return True

    main_diagonal_winner = all([matrix[index][index] == player_symbol for index in range(len(matrix))])
    diagonal_winner = all(
        [matrix[(len(matrix)) - 1 - col_index][col_index] == player_symbol for col_index in range(len(matrix))])

    if main_diagonal_winner or diagonal_winner:
        return True

    return False


def play_turn(player_symbol, row, col, matrix, turns_count):
    matrix[row][col] = player_symbol
    if turns_count >= 5:
        print_board(matrix)
        return is_winner(player_symbol, matrix)
    print_board(matrix)


def save_game(winner_name):
    with open("result.txt") as file:
        lines = file.readlines()
    content = ""
    is_new = True
    for line in lines:
        name, score = line.split(",")
        score = score[:-1]
        if name.lower() == winner_name.lower():
            score = int(score) + 1
            is_new = False
        content += f'{name},{score}\n'
    if is_new:
        content += f"{winner_name},1\n"
    with open("result.txt", "w") as file:
        file.write(content)


def show_stats():
    pass


player1_name = input("Player 1, enter your name: ")
player2_name = input("Player 2, enter your name: ")

symbol = input("Player 1, select your symbol X or O: ")
while True:

    if symbol not in ["X", "O", "o", "x"]:
        symbol = input("Player 1, select your symbol X or O: ")
    else:
        break

player1_symbol = symbol.upper()
player2_symbol = "O" if player1_symbol == "X" else "X"

position_matrix = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
for row in position_matrix:
    print(f"|  {'  |  '.join([str(el) for el in row])}  |")

print(f"{player1_name} start first!")

position_mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}
matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

player_to_symbol = {
    player1_name: player1_symbol,
    player2_name: player2_symbol
}

turns_count = 1

while True:
    current_player_name = player2_name if turns_count % 2 == 0 else player1_name
    position = obtain_valid_position(current_player_name, matrix)
    row, col = position_mapper[position]
    player_symbol = player_to_symbol[current_player_name]
    winner = play_turn(player_symbol, row, col, matrix, turns_count)
    if winner:
        # print_board(matrix)
        print(f'{current_player_name} is winner!')
        save_game(current_player_name)
        break
    turns_count += 1
    if turns_count == 10:
        # print_board(matrix)
        print("No winner - game over")
        break
