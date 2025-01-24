def operate(operator, *args):
    def sum_nums():
        return sum(args)

    def sub_nums():
        result = 0
        for el in args:
            result -= el
        return result

    def mul_nums():
        result = 1
        for el in args:
            result *= el
        return result

    def div_nums():
        result = args[0]
        for el in args[1:]:
            result /= el
        if ".0" in str(result):
            result = round(result)
        return result

    if operator == "+":
        return sum_nums()
    elif operator == "-":
        return sub_nums()
    elif operator == "*":
        return mul_nums()
    else:
        return div_nums()


print(operate("/", 8, 7))
