def classify_books(*args, **kwargs):
    fiction = {}
    non_fiction = {}

    for fic, book in args:
        if fic == "fiction":
            fiction[book] = ""
        elif fic == "non_fiction":
            non_fiction[book] = ""

    for sku, book in kwargs.items():
        if book in fiction:
            fiction[book] = sku
        elif book in non_fiction:
            non_fiction[book] = sku

    fiction_sort = sorted([(sku, book) for book, sku in fiction.items()], key=lambda x: x[0])
    non_fiction_sort = sorted([(sku, book) for book, sku in non_fiction.items()], key=lambda x: x[0], reverse=True)

    result = []

    if fiction_sort:
        result.append("Fiction Books:")
        for sku, book in fiction_sort:
            result.append(f"~~~{sku}#{book}")

    if non_fiction_sort:
        result.append("Non-Fiction Books:")
        for sku, book in non_fiction_sort:
            result.append(f'***{sku}#{book}')

    return "\n".join(result)


print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))

print(classify_books(
    ("non_fiction", "The Art of War"),
    ("fiction", "The Great Gatsby"),
    ("non_fiction", "A Brief History of Time"),
    ("fiction", "Brave New World"),
    FF1234HH="The Great Gatsby",
    NF3845UU="A Brief History of Time",
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))

print(classify_books(
    ("fiction", "Brave New World"),
    ("fiction", "The Catcher in the Rye"),
    ("fiction", "1984"),
    FICCITRZZ="The Catcher in the Rye",
    FIC1984XX="1984",
    FICBNWYYY="Brave New World"
))

print(classify_books(
    ("non_fiction", "Sapiens"),
    ("non_fiction", "Homo Deus"),
    ("non_fiction", "The Selfish Gene"),
    NF123ABC="Sapiens",
    NF987XYZ="Homo Deus",
    NF456DEF="The Selfish Gene"
))
