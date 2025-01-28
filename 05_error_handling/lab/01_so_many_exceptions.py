# numbers_list = list(map(int, input().split(", ")))
# result = 1
# number = ""
#
# for i in range(len(numbers_list)):
#     number = numbers_list[i]
#     if number <= 5:
#         result *= number
#     elif 5 < number <= 10:
#         result /= number
#
# print(result)

try:
    print(int(input("Input number:")))
except ValueError as ex:  # ex - променлива
    print(ex)