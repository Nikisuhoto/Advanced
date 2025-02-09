from collections import deque

strength = list(map(int, input().split()))
accuracy = deque(map(int, input().split()))
goals = 0

while strength and accuracy:
    current_sum = 0

    current_strength = strength.pop()
    current_accuracy = accuracy.popleft()
    current_sum = current_accuracy + current_strength

    if current_sum == 100:
        goals += 1

    elif current_sum < 100:
        if current_strength < current_accuracy:
            accuracy.appendleft(current_accuracy)
        elif current_strength > current_accuracy:
            strength.append(current_strength)
        elif current_strength == current_accuracy:
            strength.append(current_strength + current_accuracy)

    elif current_sum > 100:
        current_strength = current_strength - 10
        strength.append(current_strength)
        accuracy.append(current_accuracy)

if goals == 3:
    print("Paul scored a hat-trick!")

if goals == 0:
    print("Paul failed to score a single goal.")

if goals > 3:
    print("Paul performed remarkably well!")

if 0 < goals < 3:  # if goals > 0 and goals > 3:
    print("Paul failed to make a hat-trick.")

if goals != 0:
    print(f"Goals scored: {goals}")

if strength:
    print(f'Strength values left: ', end='')
    print(*strength, sep=", ")

if accuracy:
    print(f'Accuracy values left: ', end='')
    print(*accuracy, sep=", ")
