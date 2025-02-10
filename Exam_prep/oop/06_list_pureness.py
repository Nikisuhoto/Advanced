from collections import deque


def best_list_pureness(numbers_list, num):
    numbers_list = deque(numbers_list)
    best_pureness = float('-inf')
    best_rotation = 0

    for rotation in range(num + 1):
        pureness = sum(index * value for index, value in enumerate(numbers_list))

        if pureness > best_pureness:
            best_pureness = pureness
            best_rotation = rotation

        numbers_list.rotate(1)

    result = f"Best pureness {best_pureness} after {best_rotation} rotations"
    return result


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
