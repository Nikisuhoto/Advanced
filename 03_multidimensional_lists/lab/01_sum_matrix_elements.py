data = input().split(', ')
row_count = int(data[0])
col_count = int(data[1])

matrix = []


for row_index in range(row_count):
    data_row = [int(el) for el in input().split(', ')]
    matrix.append(data_row)

sum_elements = 0

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        sum_elements += matrix[row_index][col_index]

print(sum_elements)
print(matrix)