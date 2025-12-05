TARGET_SYMBOL = '@'
ACCESSED_SYMBOL = 'x'
NEIGHBOR_THRESHOLD = 4

def read_matrix_from_file(file_path):
    """Reads the input file and converts it into a 2D character grid."""
    with open(file_path) as file:
        return [list(line.strip()) for line in file if line.strip()]

def count_neighbor_rolls(matrix, row, col):
    """
    Counts how many '@' symbols surround a given coordinate (row, col).
    Checks all 8 directions (horizontal, vertical, diagonal).
    """
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    count = 0
    for dr, dc in directions:
        r = row + dr
        c = col + dc
        if 0 <= r <len(matrix) and 0 <=c < len(matrix[0]):
            if matrix[r][c] == TARGET_SYMBOL:
                count += 1
    return count

# --- Main Execution ---

grid = read_matrix_from_file("Day04/input.txt")

total_changes = 0
changes_in_round = -1
#Loop until no more changes occur
while True:
    changes_in_round = 0

    # Create a copy of the current grid to track changes and not affect ongoing checks
    next_grid = [row[:] for row in grid]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Only process if it's a paper roll ('@') and meets the access condition
            if grid[row][col] == TARGET_SYMBOL and count_neighbor_rolls(grid, row, col) < NEIGHBOR_THRESHOLD:
                next_grid[row][col] = ACCESSED_SYMBOL
                changes_in_round += 1

    total_changes += changes_in_round

    # Update the main grid for the next iteration
    grid = next_grid
    # Break if no changes occurred in this round
    if changes_in_round == 0:
        break

print(f"Total accessible rolls: {total_changes}")