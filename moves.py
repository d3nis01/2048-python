GRID_SIZE = 4

def slide_and_merge(row):
    new_row = [value for value in row if value != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [value for value in new_row if value != 0]
    return new_row + [0] * (GRID_SIZE - len(new_row))

def move_left(board):
    moved = False

    for r in range(GRID_SIZE):
        row = board[r]
        new_row = slide_and_merge(row)
        if board[r] != new_row:
            moved = True
        board[r] = new_row

    return moved

def move_right(board):
    moved = False

    for r in range(GRID_SIZE):
        row = board[r]
        row = row[::-1]
        new_row = slide_and_merge(row)
        new_row = new_row[::-1]
        if board[r] != new_row:
            moved = True
        board[r] = new_row

    return moved

def move_up(board):
    moved = False

    for c in range(GRID_SIZE):
        col = [board[r][c] for r in range(GRID_SIZE)]
        new_col = slide_and_merge(col)
        for r in range(GRID_SIZE):
            if board[r][c] != new_col[r]:
                moved = True
            board[r][c] = new_col[r]

    return moved

def move_down(board):
    moved = False

    for c in range(GRID_SIZE):
        col = [board[r][c] for r in range(GRID_SIZE)]
        col = col[::-1]
        new_col = slide_and_merge(col)
        new_col = new_col[::-1]
        for r in range(GRID_SIZE):
            if board[r][c] != new_col[r]:
                moved = True
            board[r][c] = new_col[r]

    return moved


def move(board, direction):
    if (direction == "LEFT"):
        return move_left(board)
    elif (direction == "RIGHT"):
        return move_right(board)
    elif (direction == "UP"):
        return move_up(board)
    elif (direction == "DOWN"):
        return move_down(board)