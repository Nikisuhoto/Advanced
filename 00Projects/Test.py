# n = int(input())
# matrix = []
# for _ in range(n):
#     row = list(map(int, input().split(', ')))
#     matrix.append(row)
# print(*matrix[0])
# print(*matrix[1])
# print(*matrix[2])
#
# diagonal_1 = []
# diagonal_2 = []
# for i in range(n):
#     diagonal_1.append(matrix[i][-1 - i])
# for i in range(n):
#     diagonal_2.append(matrix[i][i])
#
# print(', '.join(str(x) for x in diagonal_2))
#
# # input:
# 3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9

#######################################################################################################################
#
# data = input().split(', ')
# rows = int(data[0])
# # cols = int(data[1])
#
# matrix = []
# result = 0
# for r in range(rows):
#     data_row = [int(el) for el in input().split(', ')]
#     matrix.append(data_row)
#
# for r in range(len(matrix)):
#     for c in range(len(matrix[r])):
#         result += matrix[r][c]
#
# print(result)
#
# for index in range(rows):
#     print(matrix[index])

# # input:
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0


#######################################################################################################################
