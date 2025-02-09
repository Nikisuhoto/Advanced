def sum_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total


print(sum_numbers(1, 2, 3))  # Изход: 6
print(sum_numbers(10, 20, 30, 40))  # Изход: 100
