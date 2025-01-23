n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    line = input().split()
    if line[0] == "END":
        break

    row, col, value = map(int, line[1:])
    if row < 0 or row >= n or col >= n or col < 0:
        print("Invalid coordinates")
        continue

    if line[0] == "Add":
        matrix[row][col] += value
    elif line[0] == "Subtract":
        matrix[row][col] -= value

[print(*r) for r in matrix]