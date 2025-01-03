import pygame

GRID_SIZE = 4
TILE_SIZE = 100
TILE_MARGIN = 10
SCREEN_SIZE = GRID_SIZE * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN
WINDOW_HEIGHT = SCREEN_SIZE

COLORS = {
    0: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

def init_game():
    board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    
    return board

def add_new_tile(board):
    pass
    
    
def move_left(board): 
    pass
    
        
def move_right(board):
    pass
    
        
def move_up(board):
    pass

def move_down(board):
    pass
    
def move(board, direction):
    if (direction == "LEFT"):
        return move_left(board)
    elif (direction == "RIGHT"):
        return move_right(board)
    elif (direction == "UP"):
        return move_up(board)
    elif (direction == "DOWN"):
        return move_down(board)

def draw_board(screen, board):
    screen.fill((187, 173, 160))
    
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            value = board[row][column]
            color = COLORS.get(value, (60, 58, 50))
            rect = pygame.Rect(
                column * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN,
                row * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN,
                TILE_SIZE, TILE_SIZE
            )
            pygame.draw.rect(screen, color, rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, WINDOW_HEIGHT))
    pygame.display.set_caption("2048")
    board = init_game()
    clock = pygame.time.Clock()

    while True:
        direction = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    direction = 'RIGHT'

        if direction:
            moved = move(board, direction)
            if moved:
                add_new_tile(board)

        draw_board(screen, board)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

