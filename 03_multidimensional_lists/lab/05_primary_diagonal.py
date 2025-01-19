n = int(input())

matrix = []


for _ in range(n):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

sum_diagonal = 0

for index in range(len(matrix)):
    sum_diagonal += matrix[index][index]

print(sum_diagonal)