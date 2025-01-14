# n = int(input())
# data = set()
#
# for _ in range(n):
#     for el in input().split():
#         data.add(el)
#
# print(*data, sep='\n')

print(*{el for _ in range(int(input())) for el in input().split()}, sep='\n')
