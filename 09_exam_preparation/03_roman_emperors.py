def list_roman_emperors(*args, **kwargs):
    successful = []
    unsuccessful = []

    for name, status in args:
        if name in kwargs:
            rule_length = kwargs[name]
            if status:
                successful.append((name, rule_length))
            else:
                unsuccessful.append((name, rule_length))

    successful.sort(key=lambda x: (-x[1], x[0]))

    unsuccessful.sort(key=lambda x: (x[1], x[0]))

    total_emperors = len(successful) + len(unsuccessful)

    result = []
    result.append(f"Total number of emperors: {total_emperors}")

    if successful:
        result.append("Successful emperors:")
        for name, rule_length in successful:
            result.append(f"****{name}: {rule_length}")

    if unsuccessful:
        result.append("Unsuccessful emperors:")
        for name, rule_length in unsuccessful:
            result.append(f"****{name}: {rule_length}")

    return '\n'.join(result)


print(
    list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False),
                        ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19, ))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19,
                          Claudius=13, ))
print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14, ))
