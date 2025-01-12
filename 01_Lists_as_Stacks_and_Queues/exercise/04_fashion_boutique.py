clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())

racks = 0

while clothes_stack:
    racks += 1
    current_rack_free_space = rack_capacity
    while clothes_stack and clothes_stack[-1] <= current_rack_free_space:
        current_rack_free_space -= clothes_stack.pop()

print(racks)
