n = int(input())

matrix = []


for _ in range(n):
    row_data = list(input())
    matrix.append(row_data)

char = input()

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == char:
            print(f'({row_index}, {col_index})')
            exit()
print(f'{char} does not occur in the matrix')