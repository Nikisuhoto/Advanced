def plant_garden(space, *allowed_plants, **requests):
    sorted_requests = sorted(requests.items(), key=lambda x: x[0])
    plants_planted = []
    all_planted = True

    for plant, quantity in sorted_requests:
        for p, s in allowed_plants:
            if plant == p:
                planted = min(quantity, int(space // s))
                if planted < quantity:
                    all_planted = False
                if planted > 0:
                    plants_planted.append((plant, planted))
                    space -= planted * s
                if space <= 0:
                    break

    result = []

    if all_planted:
        result.append(f"All plants were planted! Available garden space: {space:.1f} sq meters.")
    else:
        result.append("Not enough space to plant all requested plants!")

    result.append("Planted plants:")
    for plant, quantity in plants_planted:
        result.append(f'{plant}: {quantity}')

    return "\n".join(result)


print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))
