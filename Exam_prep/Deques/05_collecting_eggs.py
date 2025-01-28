from collections import deque

boxes = 0
eggs = deque(map(int, input().split(", ")))
paper = deque(map(int, input().split(", ")))

while len(eggs) > 0 and len(paper) > 0:

    current_egg = eggs.popleft()
    current_paper = paper[-1]

    if current_egg <= 0:
        continue
    if current_egg == 13:
        if len(paper) > 1:
            paper[0], paper[-1] = paper[-1], paper[0]
        continue

    if current_paper + current_egg <= 50:
        boxes += 1
        paper.pop()
    elif current_paper + current_egg > 50:
        paper.pop()

if boxes >= 1:
    print(f"Great! You filled {boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print("Eggs left: ", end="")
    # for egg in eggs:
    #     print(", ".join(map(str(egg))))
    print(*eggs, sep=", ")
if paper:
    print("Pieces of paper left: ", end="")
    # for p in paper:
    #     print(", ".join(map(str(p))))
    print(*paper, sep=", ")
