
def list_manipulator(numbers_list, command_1, command_2, *args):

    if command_1 == "remove":

        if command_2 == "beginning":
            if len(args) == 1:
                for index in range(*args):
                    numbers_list.pop(0)
                return numbers_list
            else:
                numbers_list.pop(0)
            return numbers_list

        if command_2 == "end":
            if len(args) == 1:
                for index in range(*args):
                    numbers_list.pop()
                return numbers_list
            else:
                numbers_list.pop()
            return numbers_list

    if command_1 == "add":
        if command_2 == "beginning":
            if len(args) == 1:
                numbers_list.insert(0, *args)
                return numbers_list
            if len(args) > 1:
                for i in range(len(args)):
                    numbers_list.insert(i, args[i])
                return numbers_list
        if command_2 == "end":
            if len(args) == 1:
                numbers_list.append(*args)
                return numbers_list
            if len(args) > 1:
                for i in range(len(args)):
                    numbers_list.append(args[i])
                return numbers_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
