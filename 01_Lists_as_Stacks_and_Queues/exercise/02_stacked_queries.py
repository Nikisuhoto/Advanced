
n = int(input())
stack = []

for _ in range(n):

    command = input().split()

    if command[0] == '1':
        number = int(command[1])
        stack.append(number)
    elif stack:
        if command[0] == '2':
            stack.pop()
        elif command[0] == '3':
            print(max(stack))
        elif command[0] == '4':
            print(min(stack))

while stack:
    print(stack.pop(), end='')
    if stack:
        print(', ', end='')