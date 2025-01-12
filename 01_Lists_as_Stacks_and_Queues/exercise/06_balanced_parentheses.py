expression = input()

opening = '([{'
closing = ')]}'
stack = []

for char in expression:
    if char in opening:
        stack.append(char)
    elif char in closing:
        if not stack:
            print('NO')
            break
        last_par = stack.pop()
        if opening.index(last_par) != closing.index(char):
            print('NO')
            break
else:
    if stack:
        print('NO')
    else:
        print('YES')