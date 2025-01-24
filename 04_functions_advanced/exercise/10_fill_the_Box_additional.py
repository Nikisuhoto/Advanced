def fill_the_box(height, lenght, width, *args):
    box_volume = height * lenght * width

    boxes = 0

    for item in args:
        if item == "Finish":
            break
        boxes += item

    if box_volume > boxes:
        return f'There is free space in the box. You could put {box_volume - boxes} more cubes.'
    return f"No more free space! You have {boxes - box_volume} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
