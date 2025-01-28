from collections import deque

bomb_effects = deque(map(int, input().split(", ")))
bomb_casings = list(map(int, input().split(", ")))
bomb_production = {}
d_bomb = 0
c_bomb = 0
s_bomb = 0
is_happy_case = False

while bomb_casings and bomb_effects:

    if d_bomb >= 3 and c_bomb >= 3 and s_bomb >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        is_happy_case = True
        break

    current_bomb_effects = bomb_effects[0]
    current_bomb_casings = bomb_casings[-1]
    try_bomb = current_bomb_casings + current_bomb_effects

    if try_bomb == 40:
        d_bomb += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif try_bomb == 60:
        c_bomb += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif try_bomb == 120:
        s_bomb += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

if is_happy_case == False:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {c_bomb}")
print(f"Datura Bombs: {d_bomb}")
print(f"Smoke Decoy Bombs: {s_bomb}")
