# Puzzle Path Finder

## Description

The `Puzzle Path Finder` is a graph traversal based solution that aims to solve a given 2-D puzzle by finding the shortest path from a source coordinate to a destination coordinate. Using graph traversal techniques, this solution efficiently navigates through a maze of empty spaces and barriers.

## Features

1. **Graph Traversal**: Utilizes Breadth First Search (BFS) to ensure the shortest path is found.
2. **Flexible Board Dimensions**: Supports any rectangular board with dimensions MxN.
3. **Barrier Recognition**: Understands and avoids barriers, denoted by `#`.
4. **Path Return**: Provides a clear list of coordinates representing the path taken, from source to destination.

## How It Works

The puzzle board is treated as a graph where each cell (either empty or barrier) is a node. Adjacent empty cells are connected, and the BFS algorithm traverses through the board to find the shortest path from the source to the destination.

## Usage

### Prerequisites

- Python 3.x

### Installation

```bash
git clone https://github.com/haleyekrueger/puzzle-path-finder.git
cd puzzle-path-finder
```

### Using the Function

```python
from Puzzle import solve_puzzle

board = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]

source = (0, 0)
destination = (4, 4)

path = solve_puzzle(board, source, destination)
print(path)
```

## Examples

Given the above puzzle:

- For source `(0,2)` and destination `(2,2)`, the output will be `[(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)]`.
- For source `(0,0)` and destination `(4,4)`, the output will be `[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]`.
- For source `(0,0)` and destination `(4,0)`, the output will be `None`.

## Limitations

- Due to the BFS nature, it always finds the shortest path but can be more time-consuming for large boards.
- Only supports two types of nodes: empty spaces and barriers.

## Contact

Haley Krueger - h.elaine.krueger@gmail.com

Project Link: https://github.com/haleyekrueger/puzzle-path-finder
