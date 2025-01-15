from collections import deque

colors_strings = deque(input().split())

mail_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}
collected_colors = []

while colors_strings:

    first_string = colors_strings.popleft()
    last_string = colors_strings.pop() if colors_strings else ""
    for color in (first_string + last_string, last_string + first_string):
        if color in mail_colors or color in secondary_colors:
            collected_colors.append(color)
            break
    else:
        if len(first_string) > 1:
            colors_strings.insert(len(colors_strings) // 2, first_string[:-1])
        if len(last_string) > 1:
            colors_strings.insert(len(colors_strings) // 2, last_string[:-1])

for color in collected_colors:
    if color in secondary_colors:
        for c in secondary_colors[color]:
            if c not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)

