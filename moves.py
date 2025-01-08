GRID_SIZE = 4

def slide_and_merge(row):
    """Slides non-zero values to the left and merge equal values"""
    new_row = [value for value in row if value != 0] # Remove zeros from row/column
    score = 0

    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            score += new_row[i]
            new_row[i + 1] = 0 # Merge by setting the next value to zero
            
    new_row = [value for value in new_row if value != 0] # Remove zeros again because of merging
    new_row = new_row + [0] * (GRID_SIZE - len(new_row)) # Fill with zeros to match GRID_SIZE

    return new_row, score

def move_left(board):
    moved = False
    move_score = 0
    
    for r in range(GRID_SIZE):
        row = board[r]
        new_row, score = slide_and_merge(row)
        
        if board[r] != new_row:
            moved = True
            move_score += score
        board[r] = new_row
    return moved, move_score

def move_right(board):
    moved = False
    move_score = 0
    
    for r in range(GRID_SIZE):
        row = board[r]
        row = row[::-1] # Reverse row because slide_and_merge works from right to left
        new_row, score = slide_and_merge(row)
        new_row = new_row[::-1] # Reverse back
        
        if board[r] != new_row:
            moved = True
            move_score += score
        board[r] = new_row
        
    return moved, move_score

def move_up(board):
    moved = False
    move_score = 0
    
    for c in range(GRID_SIZE):
        col = [board[r][c] for r in range(GRID_SIZE)] # Get column as a list
        new_col, score = slide_and_merge(col)
        
        if col != new_col:
            moved = True
            move_score += score
        
            for r in range(GRID_SIZE):
                board[r][c] = new_col[r]
        
    return moved, move_score


def move_down(board):
    moved = False
    move_score = 0
    
    for c in range(GRID_SIZE):
        col = [board[r][c] for r in range(GRID_SIZE)] # Get column as a list
        col = col[::-1] # Reverse column because slide_and_merge works from right to left
        new_col, score = slide_and_merge(col)
        new_col = new_col[::-1] # Reverse back
        col = col[::-1] # Reverse back to check if column has changed
        
        if col != new_col: # Check if column has changed
            moved = True
            move_score += score
            
            for r in range(GRID_SIZE):
                board[r][c] = new_col[r] # Update column in board
        
    return moved, move_score

def move(board, direction):
    """Moves the board in the specified direction"""
    if direction == "LEFT":
        return move_left(board)
    elif direction == "RIGHT":
        return move_right(board)
    elif direction == "UP":
        return move_up(board)
    elif direction == "DOWN":
        return move_down(board)
