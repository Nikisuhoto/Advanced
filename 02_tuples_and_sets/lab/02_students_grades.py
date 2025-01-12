n = int(input())

students = {}

for _ in range(n):
    name, grade_str = tuple(input().split())
    grade = float(grade_str)
    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    form_gr = [str(f'{grade:.2f}') for grade in grades]
    avr_gr = sum(grades)/len(grades)
    print(f'{name} -> {" ".join(form_gr)} (avg: {avr_gr:.2f})')
