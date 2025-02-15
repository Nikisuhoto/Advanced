# from collections import deque
#
# substances = list(map(int, input().split(", ")))
# energy = deque(map(int, input().split(", ")))
# potions = []
#
# while substances and energy and len(potions) < 5:
#     current_substances = substances.pop()
#     current_energy = energy.popleft()
#
#     try_for_potion = current_substances + current_energy
#
#     if try_for_potion == 110:
#         if "Brew of Immortality" not in potions:
#             potions.append("Brew of Immortality")
#             try_for_potion = 0
#
#     if try_for_potion >= 100:
#         if "Essence of Resilience" not in potions:
#             if (current_substances + current_energy) - 100 > 0:
#                 energy.append((current_substances + current_energy) - 100)
#             potions.append("Essence of Resilience")
#             try_for_potion = 0
#         # continue
#
#     if try_for_potion >= 90:
#         if "Draught of Wisdom" not in potions:
#             if (current_substances + current_energy) - 100 > 0:
#                 energy.append((current_substances + current_energy) - 90)
#             potions.append("Draught of Wisdom")
#             try_for_potion = 0
#         # continue
#
#     if try_for_potion >= 80:
#         if "Potion of Agility" not in potions:
#             if (current_substances + current_energy) - 100 > 0:
#                 energy.append((current_substances + current_energy) - 80)
#             potions.append("Potion of Agility")
#             try_for_potion = 0
#         # continue
#
#     if try_for_potion >= 70:
#         if "Elixir of Strength" not in potions:
#             if (current_substances + current_energy) - 100 > 0:
#                 energy.append((current_substances + current_energy) - 70)
#             potions.append("Elixir of Strength")
#             try_for_potion = 0
#         # continue
#
#
#
# print(potions)
# print(substances)
# print(energy)


from collections import deque


potions = {
    "Brew of Immortality": 110,
    "Essence of Resilience": 100,
    "Draught of Wisdom": 90,
    "Potion of Agility": 80,
    "Elixir of Strength": 70
}
crafted_potions = []

substances = list(map(int, input().split(", ")))
energy_crystals = deque(map(int, input().split(", ")))


while substances and energy_crystals:
    current_substance = substances.pop()
    current_crystal = energy_crystals.popleft()
    total_energy = current_substance + current_crystal

    for p, e in potions.items():
        if e == total_energy and p not in crafted_potions:
            crafted_potions.append(p)
            break
    else:
        possible_potions = [e for e in potions.values() if
                            e < total_energy and e not in [potions[p] for p in crafted_potions]]
        if possible_potions:
            highest_possible = max(possible_potions)
            crafted_potions.append([p for p, e in potions.items() if e == highest_possible][0])
            if current_crystal - 20 > 0:
                energy_crystals.append(current_crystal - 20)
        else:
            if current_crystal - 5 > 0:
                energy_crystals.append(current_crystal - 5)

    if len(crafted_potions) == 5:
        print("Success! The alchemist has forged all potions!")
        print(f"Crafted potions: {', '.join(crafted_potions)}")
        break

else:
    print("The alchemist failed to complete his quest.")
    if crafted_potions:
        print(f"Crafted potions: {', '.join(crafted_potions)}")

if substances:
    print(f"Substances: {', '.join(map(str, substances[::-1]))}")
if energy_crystals:
    print(f"Crystals: {', '.join(map(str, energy_crystals))}")
