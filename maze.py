import sys
from astar import astar

def build_maze(text):
    """Builds maze list from input string """
    maze = []
    lines = text.split()

    for line in lines:
        row = []
        row[:] = line
        maze.append(row)

    return maze

def find_start(maze):
    """Finds entrace at the top"""
    return (0,maze[0].index('_'))

def find_end(maze):
    """Finds exit at the bottom row"""
    return (len(maze)-1,maze[-1].index('_'))

def build_solved_maze(maze, path):
    """Fills maze with alphabet path using list of coords touples as solved path"""
    if path is None:
        print("Doesn't seem like this maze has a solution.")
        return []

    alphabet = list(map(chr, range(97, 123)))

    for i, step in enumerate(path):
        maze[step[0]][step[1]] = alphabet[i % len(alphabet)]
    
    return maze

def print_solved_maze(solved_maze):
    """Iterates through the solved maze list and prints it out"""
    print()

    for row in solved_maze:
        for cell in row:
            print(cell, end="")
        print()
    
    print()


# unit tests

def main():

    text = sys.stdin.read()

    maze = build_maze(text)

    start = find_start(maze)
    end = find_end(maze)

    path = astar(maze, start, end)
    solved_maze = build_solved_maze(build_maze(text), path)

    print_solved_maze(solved_maze)


if __name__ == '__main__':
    main()
