data = input().split(', ')
row_count = int(data[0])
col_count = int(data[1])

matrix = []

for _ in range(row_count):
    data_row = [int(el) for el in input().split(', ')]
    matrix.append(data_row)

max_sum = float('-inf')
elements = []
for row_index in range(len(matrix) - 1):
    for col_index in range(len(matrix[row_index]) - 1):
        current_el = matrix[row_index][col_index]
        next_to_current = matrix[row_index][col_index + 1]
        element_below_current = matrix[row_index + 1][col_index]
        element_diagonal_current = matrix[row_index + 1][col_index + 1]

        current_sum = current_el + next_to_current + element_below_current + element_diagonal_current

        if current_sum > max_sum:
            max_sum = current_sum
            elements = [
                [current_el, next_to_current],
                [element_below_current, element_diagonal_current]
            ]

print(*elements[0])
print(*elements[1])
print(max_sum)