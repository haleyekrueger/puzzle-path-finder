from collections import deque

def check_validity(puzzle, x, y):
    # if cell is empty or cell is not on puzzle board return false
    if x < 0 or x >= len(puzzle) or y < 0 or y >= len(puzzle[0]):
        return False
    if puzzle[x][y] == '#':     # check for obstructions
        return False
    return True
    
def solve_puzzle(board, source, destination):

    print('board: ', board)
    print('source: ', source)
    print('desintation: ', destination)
    # use a deque for breadth first search traversal
    queue = deque([(source, [source])])  # (cell, path_til_now)

    # Create a set to keep track of visited cells
    visited = set([source])

    # possible directions
    directions = {'left': (0, -1), 'right': (0, 1), 'down': (-1, 0), 'up': (1, 0)}

    while queue:
        # pop current cell coordinates and the path up until now
        current, path_til_now = queue.popleft()

        # check if destination has been reached
        if current == destination:
            return path_til_now

        x, y = current

        # go up, down, left, right
        for dir, (dir_x, dir_y) in directions.items():
            print(dir_x, dir_y)
            new_x, new_y = x + dir_x, y + dir_y     # move the coordinates in that direction

            # check validity of the move
            if check_validity(board, new_x, new_y) and (new_x, new_y) not in visited:
                # append the new cell and path up until now to the queue
                queue.append(((new_x, new_y), path_til_now + [(new_x, new_y)]))
                visited.add((new_x, new_y)) # mark it as visited

    # if no path works, return None
    return None
