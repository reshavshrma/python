from random import randint
from math import ceil


def start_game(sudoku_state, positions):
    display(sudoku_state)
    
    for r, c in positions:
        sudoku_state[r][c] = int(input(f"For row {r+1} and col {c+1} i.e {(r+1, c+1)}"))
    return sudoku_state
    
    
def end_game(sudoku_state):
    print("You won the game !!!!")
    display(sudoku_state)


def fill_grid(size):
    sudoku_state = [list(' ' * size) for _ in range(size)]
    p = set(range(1, size + 1))
    for r in range(size):
        for c in range(size):
            n = randint(1, size)
            a = set(sudoku_state[r] + [row[c] for row in sudoku_state])
            candidate = list(p - a)
            if candidate:
                sudoku_state[r][c] = candidate[randint(0, len(candidate) - 1)]
            else:
                return fill_grid(size)
    return sudoku_state


def display(grid):
    size = len(grid)
    hr_line = '--' * size + '-'
    print(hr_line)
    for r in range(size):
        fs = '{}|' * size
        fs = '|' + fs
        print(fs.format(*grid[r]))
        print(hr_line)


def initialize():
    size = int(input("Enter Grid Size : "))
    sudoku_state = fill_grid(size)
    
    game_level = {1: ('Very Easy', 20), 2: ('Easy', 35), 3: ('Medium', 50), 4: ('Hard', 60), 5: ('Very Hard', 75)}
    print("There are ", len(game_level), "levels : ")
    for level, info in game_level.items():
        print(f"Level {level}: {info[0]}")

    level = int(input("Enter game level between (1 to 5)"))
    no_of_hidden_fields = ceil(game_level[level][1] * size * size / 100)
    
    positions = []
    p = list(range(size * size))
    for _ in range(no_of_hidden_fields):
        position = p.pop(randint(0, len(p) - 1))
        positions.append((position // size, position % size))

    for r, c in positions:
        sudoku_state[r][c] = 'X'
    
    return sudoku_state, positions


def sudoku():
    sudoku_state, positions = initialize()
    sudoku_state = start_game(sudoku_state, positions)
    end_game(sudoku_state)


sudoku()
