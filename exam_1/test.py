# Read the size of the grid
N = int(input())

# Initialize the grid
grid = []
pacman_pos = None
stars_count = 0
ghosts_count = 0
freezers_count = 0

# Read the grid and find Pacman's position, stars, ghosts, and freezers
for i in range(N):
    row = list(input().strip())
    grid.append(row)
    if 'P' in row:
        pacman_pos = (i, row.index('P'))
    stars_count += row.count('*')
    ghosts_count += row.count('G')
    freezers_count += row.count('F')

# Initialize Pacman's health and immunity
health = 100
immunity = False

# Directions mapping
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Function to handle Pacman's movement
while True:
    command = input().strip()
    if command == "end":
        break

    # Calculate new position
    dx, dy = directions[command]
    new_row = (pacman_pos[0] + dx) % N
    new_col = (pacman_pos[1] + dy) % N

    # Mark the current position as empty
    grid[pacman_pos[0]][pacman_pos[1]] = '-'

    # Check the new position
    cell = grid[new_row][new_col]
    if cell == '*':
        stars_count -= 1
        grid[new_row][new_col] = '-'
    elif cell == 'G':
        if not immunity:
            health -= 50
            if health <= 0:
                health = 0
                break
        else:
            immunity = False
        grid[new_row][new_col] = '-'
    elif cell == 'F':
        immunity = True
        grid[new_row][new_col] = '-'

    # Update Pacman's position
    pacman_pos = (new_row, new_col)

    # Check if all stars are collected
    if stars_count == 0:
        break

# Output the result
if health == 0:
    print(f"Game over! Pacman last coordinates [{pacman_pos[0]},{pacman_pos[1]}]")
elif stars_count == 0:
    print("Pacman wins! All the stars are collected.")
else:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")
if stars_count > 0:
    print(f"Uncollected stars: {stars_count}")

# Mark Pacman's final position on the grid
grid[pacman_pos[0]][pacman_pos[1]] = 'P'

# Print the final grid
for row in grid:
    print(''.join(row))