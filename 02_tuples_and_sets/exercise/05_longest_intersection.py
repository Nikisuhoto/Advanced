longest_intersection = set()

n = int(input())

for _ in range(n):
    first_range, second_range = input().split('-')
    first_start, first_end = [int(x) for x in first_range.split(',')]
    second_start, second_end = [int(x) for x in second_range.split(',')]

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    current_inter = first_set & second_set

    if len(current_inter) > len(longest_intersection):
        longest_intersection = current_inter

print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')
