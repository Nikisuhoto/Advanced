def naughty_or_nice_list(*args, **kwargs):
    nice_kids = []
    naughty_kids = []
    not_found = []

    for i, j in args[0]:
        for ref in args:
            if str(i) in ref:
                if "Nice" in ref:
                    nice_kids.append(j)
                elif "Naughty" in ref:
                    naughty_kids.append(j)
                else:
                    not_found.append(j)

    for _, name in args[0]:
        if name not in nice_kids and name not in naughty_kids:
            not_found.append(name)

    for name, staus in kwargs.items():
        if name in nice_kids:
            nice_kids.remove(name)
            if staus == "Nice":
                nice_kids.append(name)
            elif staus == "Naughty":
                naughty_kids.append(name)

    if nice_kids:
        result = "Nice: "
        result += ", ".join(nice_kids)
    if naughty_kids:
        result += "\nNaughty: "
        result += ", ".join(naughty_kids)
    if not_found:
        result += "\nNot found: "
        result += ", ".join(not_found)

    return result


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
