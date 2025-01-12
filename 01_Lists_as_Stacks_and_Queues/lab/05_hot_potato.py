from collections import deque

kids = deque(input().split())
n = int(input()) - 1

while len(kids) > 1:

    kids.rotate(-n)
    rem_kid = kids.popleft()
    print(f'Removed {rem_kid}')

print(f'Last is {kids[0]}')

