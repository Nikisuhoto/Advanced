# def even_odd(*args):
#     command = args[-1]
#     if command == "even":
#         return [x for x in args[:-1] if x % 2 == 0]
#     return [x for x in args[:-1] if x % 2 != 0]


def even_odd(*args):
    result = []
    if args[-1] == "even":
        for numbs in args[:-1]:
            if numbs % 2 == 0:
                result.append(numbs)
    else:
        for nums in args[:-1]:
            if nums % 2 != 0:
                result.append(nums)

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
