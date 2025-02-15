def naughty_or_nice_list(kids_list, *commands, **name_status):
    nice_kids = []
    naughty_kids = []

    for command in commands:
        number, status = command.split("-")
        number = int(number)
        matching_kids = [kid for kid in kids_list if kid[0] == number]

        if len(matching_kids) == 1:
            kid = matching_kids[0]
            kids_list.remove(kid)
            if status == "Nice":
                nice_kids.append(kid[1])
            else:
                naughty_kids.append(kid[1])

    for name, status in name_status.items():

        matching_kids = [kid for kid in kids_list if kid[1] == name]

        if len(matching_kids) == 1:
            kid = matching_kids[0]
            kids_list.remove(kid)
            if status == "Nice":
                nice_kids.append(name)
            else:
                naughty_kids.append(name)

    not_found = [kid[1] for kid in kids_list]

    result = []
    if nice_kids:
        result.append(f"Nice: {', '.join(nice_kids)}")
    if naughty_kids:
        result.append(f"Naughty: {', '.join(naughty_kids)}")
    if not_found:
        result.append(f"Not found: {', '.join(not_found)}")

    return "\n".join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
