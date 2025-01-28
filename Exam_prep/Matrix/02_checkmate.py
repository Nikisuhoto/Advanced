matrix = []

# Въвеждаме 8 реда
for i in range(8):
    row = input().split()  # Разделяме входа по интервали
    matrix.append(row)  # Добавяме реда в матрицата

queen_positions = []  # Тук ще съхраняваме позициите на всички кралици
king_position = []  # Тук ще съхраняваме позицията на краля

# Обхождаме всички клетки на дъската
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "Q":
            queen_positions.append((row, col))  # Добавяме позицията на кралицата (ред, колона)
        if matrix[row][col] == "K":
            king_position = (row, col)  # Записваме позицията на краля

queen_attack = []  # Тук ще съхраняваме всички кралици, които застрашават краля

# Обхождаме всяка кралица и проверяваме дали тя застрашава краля
for queen in queen_positions:
    row_queen, col_queen = queen  # Позицията на кралицата (ред, колона)
    row_king, col_king = king_position  # Позицията на краля (ред, колона)

    # Проверка дали кралицата е в същия ред с краля
    if row_queen == row_king:
        # Проверка дали няма кралица, която да блокира атаката по реда
        if col_queen < col_king:  # Кралицата е наляво от краля
            blocked = any(
                matrix[row_queen][i] == 'Q' for i in range(col_queen + 1, col_king))  # Проверяваме блокаж вдясно
        else:  # Кралицата е надясно от краля
            blocked = any(
                matrix[row_queen][i] == 'Q' for i in range(col_king + 1, col_queen))  # Проверяваме блокаж вляво

        if not blocked:
            queen_attack.append(queen)  # Кралицата може да застраши краля

    # Проверка дали кралицата е в същата колона с краля
    elif col_queen == col_king:
        # Проверка дали няма кралица, която да блокира атаката по колоната
        if row_queen < row_king:  # Кралицата е над краля
            blocked = any(
                matrix[i][col_queen] == 'Q' for i in range(row_queen + 1, row_king))  # Проверяваме блокаж надолу
        else:  # Кралицата е под краля
            blocked = any(
                matrix[i][col_queen] == 'Q' for i in range(row_king + 1, row_queen))  # Проверяваме блокаж нагоре

        if not blocked:
            queen_attack.append(queen)  # Кралицата може да застраши краля

    # Проверка дали кралицата е на диагонала с краля
    elif abs(row_queen - row_king) == abs(col_queen - col_king):  # Проверка за диагонал
        # Проверка по диагонала
        step_r = 1 if row_queen < row_king else -1  # Стъпка за реда (нагоре или надолу)
        step_c = 1 if col_queen < col_king else -1  # Стъпка за колоната (наляво или надясно)

        r, c = row_queen + step_r, col_queen + step_c
        blocked = False
        while r != row_king and c != col_king:
            if matrix[r][c] == 'Q':  # Ако има кралица по диагонала
                blocked = True
                break
            r += step_r
            c += step_c

        if not blocked:
            queen_attack.append(queen)  # Кралицата може да застраши краля

# Ако има кралици, които застрашават краля
if queen_attack:
    for attack in queen_attack:
        print(list(attack))  # Принтиране на координатите на кралиците
else:
    print("The king is safe!")  # Ако няма кралици, които да застрашават краля
