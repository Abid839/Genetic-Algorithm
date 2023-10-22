import random
import os
import time
import math

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
VISITED = []


def generate_random_grid():
    choices = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    initial_grid = []
    for i in range(3):
        grid = []
        for j in range(3):
            num = random.choice(choices)  # Choose a random number from choices
            choices.remove(num)  # Remove the chosen number from choices
            grid.append(num)
        initial_grid.append(grid)
    return initial_grid


def misplaced_tiles(board):
    # Calculate the number of misplaced tiles heuristic
    row = len(board)
    col = len(board)
    h = 0
    for i in range(row):
        for j in range(col):
            if board[i][j] != goal[i][j]:
                h += 1
    return h


def manhattan_distance(board):
    # Calculate the Manhattan distance heuristic
    h = 0
    for i in range(3):
        for j in range(3):
            value = board[i][j]
            if value != 0:
                target_row = (value - 1) // 3
                target_col = (value - 1) % 3
                h += abs(i - target_row) + abs(j - target_col)
    return h


def find_blank(board):
    # Find the coordinates of the blank (zero) tile on the board
    row = len(board)
    col = len(board)
    for i in range(row):
        for j in range(col):
            if board[i][j] == 0:
                return i, j


def move_valid(x, y):
    # check if the applied moves are valid
    return 0 <= x <= 2 and 0 <= y <= 2


def apply_move(board, blank_x, blank_y, applied_x, applied_y, heuristics):
    temp_board = [list(row) for row in board]
    temp_num = board[applied_x][applied_y]
    temp_board[applied_x][applied_y] = 0
    temp_board[blank_x][blank_y] = temp_num

    return temp_board


def calc_entropy(state_list, parent_state, iterations, cost_function):
    all_entropy = []
    T = 0.25 * iterations
    parent_h = cost_function(parent_state)
    print(f"STATE {state_list}")
    for state in state_list:
        child_h = cost_function(state)
        print(f"PARENT {parent_h} CHILD {child_h}")
        delta = parent_h - child_h

        T = T - 0.25
        if T == 0:
            return None
        else:
            ent = math.exp(delta / T)
            all_entropy.append(ent)
    print(f"ENTROPY LIST {all_entropy}")
    index = all_entropy.index(max(all_entropy))
    return state_list[index]


def solve(current_state, heuristics, itter, cost_function):
    entropy_list = []
    OPEN = []
    equal_list = []

    blank_x, blank_y = find_blank(current_state)
    for i in moves:
        new_x = blank_x + i[0]
        new_y = blank_y + i[1]
        if move_valid(new_x, new_y):
            temp_board = apply_move(current_state, blank_x, blank_y, new_x, new_y, heuristics)
            print(temp_board)

            if temp_board not in VISITED:
                OPEN.append(temp_board)

    if len(OPEN) == 0:
        
        print("no items")
        return None
    else:

        for i in OPEN:
            parent_h = cost_function(current_state)
            child_h = cost_function(i)
            if parent_h - child_h > 0:
                VISITED.append(current_state)
                return i
            elif parent_h - child_h == 0:
                equal_list.append(i)
            else:
                entropy_list.append(i)

        if len(equal_list) != 0:
            VISITED.append(current_state)
            return equal_list[0]
        else:
            VISITED.append(current_state)
            return calc_entropy(entropy_list, current_state, itter, cost_function)


def main():
    ITERATIONS = 50000
    heuristics = 1
    running = True
    # current_state = [[1, 2, 7], [8, 6, 0], [5, 4, 3]]
    # current_state = [[1, 3, 7],[6, 0, 8],[4, 2, 5]]
    # current_state = [[2, 8, 6], [7, 1, 3], [5, 0, 4]]
    current_state = generate_random_grid()
    print("CURRENT STATE")
    for i in current_state:
        print(i)
    step = 0
    while running:
        if current_state is not None:
            print("CURRENT")
            for i in current_state:
                print(i)

        # print(f"ITERATIONS {ITERATIONS}")
        ITERATIONS -= 1
        step += 1
        if ITERATIONS == 0 or current_state is None:
            print("NO Solution")
            print(len(VISITED))
            print(f"ITERATIONS {ITERATIONS}")
            running = False
        elif current_state == goal:
            print("REACHED \n")
            print("GOAL")
            for i in current_state:
                print(i)
            running = False
        else:
            current_state = solve(current_state, heuristics, ITERATIONS, misplaced_tiles)

    # print(f"STEPS {step}")


if __name__ == "__main__":
    main()
