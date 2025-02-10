from collections import deque

max_caffeine = 300
total_caffeine = 0

milligrams_caffeine = list(map(int, input().split(", ")))
energy_drinks = deque(map(int, input().split(", ")))

while milligrams_caffeine and energy_drinks:
    current_caffeine = 0
    current_milligrams = milligrams_caffeine.pop()
    current_energy_drinks = energy_drinks.popleft()

    current_caffeine += current_milligrams * current_energy_drinks
    total_caffeine += current_caffeine
    if total_caffeine > max_caffeine:
        if current_caffeine + total_caffeine > max_caffeine:
            energy_drinks.append(current_energy_drinks)
            total_caffeine -= current_caffeine
            total_caffeine -= 30
            if total_caffeine < 0:
                total_caffeine = 0

if energy_drinks:
    print(f'Drinks left: ', end='')
    print(*energy_drinks, sep=", ")
    print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
    print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
