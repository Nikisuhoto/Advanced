from modules_nine.lab.math_operations_core import execute

expression = input()

number1, sign, number2 = expression.split()
number1 = float(number1)
number2 = float(number2)

result = execute(number1, sign, number2)
print(f'{result:.2f}')
