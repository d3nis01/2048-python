import pygame
import random
from moves import *
import sys

# Constants for game configuration
GRID_SIZE = 4
TILE_SIZE = 100
TILE_MARGIN = 10
INFO_HEIGHT = 100
SCREEN_SIZE = GRID_SIZE * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN
WINDOW_HEIGHT = SCREEN_SIZE + INFO_HEIGHT

# Color scheme for tiles
COLORS = {
    0: (103, 145, 153),
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

background_color = (30, 100, 119)
font_color =(119, 110, 101)

# Fonts for text rendering
pygame.font.init()
FONT = pygame.font.Font(None, 40)
INFO_FONT = pygame.font.Font(None, 40)
GAME_OVER_FONT = pygame.font.Font(None, 50)

def init_game():
    board = []
    for counter in range(GRID_SIZE):
        row = [0] * GRID_SIZE 
        board.append(row)
    return board

def add_new_tile(board):
    empty_tiles = []

    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            if board[row][column] == 0:
                empty_tiles.append((row, column))
    
    if empty_tiles:
        r, c = random.choice(empty_tiles)
        
        if random.random() < 0.9:
            board[r][c] = 2
        else:
            board[r][c] = 4

def is_game_over(board):
    """Checks if there are no valid moves left on the board"""
    
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            if board[row][column] == 0: # The game is not over if there are empty tiles
                return False  
            
            #Check if two tiles are the same and can merge vertically (up and down)
            if row < GRID_SIZE - 1 and board[row][column] == board[row + 1][column]:
                return False  
            
            #Check if two tiles are the same and can merge horizontally (left and right)            
            if column < GRID_SIZE - 1 and board[row][column] == board[row][column + 1]:
                return False

    return True


def get_highest_tile(board):
    """Returns the highest tile value on the board"""
    highest = 0
    for row in board:
        for tile in row:
            if tile > highest: 
                highest = tile
    return highest


def draw_board(screen, board, score, moves, game_over=False):
    """Draws the game board, tiles, and game information on the screen"""
    screen.fill(background_color)

    # Draw each tile on the board
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            value = board[r][c]
            color = COLORS.get(value, (255, 255, 255))
            current_tile = pygame.Rect(
                c * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN,  
                r * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN + INFO_HEIGHT,
                TILE_SIZE, TILE_SIZE
            ) # left, top, width, height
            pygame.draw.rect(screen, color, current_tile)
            if value:
                text = FONT.render(str(value), True, font_color)
                text_rect = text.get_rect(center=current_tile.center)
                screen.blit(text, text_rect)

    # Display score, moves, and highest tile
    highest_tile = get_highest_tile(board)
    score_text = INFO_FONT.render(f"Score: {score}", True, (255, 255, 255))
    moves_text = INFO_FONT.render(f"Moves: {moves}", True, (255, 255, 255))
    highest_text = INFO_FONT.render(f"Highest Tile: {highest_tile}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))
    screen.blit(moves_text, (SCREEN_SIZE - 200, 20))
    screen.blit(highest_text, (20, 60))

    # Show "Game Over" message if the game is finished
    if game_over:
        game_over_text = GAME_OVER_FONT.render("Game Over!", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(
            center=(SCREEN_SIZE // 2, (WINDOW_HEIGHT + INFO_HEIGHT) // 2)
        )
        screen.blit(game_over_text, text_rect)

def main():
    """Main game loop for 2048."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, WINDOW_HEIGHT))
    pygame.display.set_caption("2048")
    
    # Initialize game variables
    board = init_game()
    score = 0
    moves = 0
    add_new_tile(board)
    add_new_tile(board)
    game_over = False

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not game_over and event.type == pygame.KEYDOWN:
                direction = None
                if event.key == pygame.K_UP:
                    direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    direction = 'RIGHT'

                if direction:
                    moved, gained_score = move(board, direction)
                    if moved:
                        add_new_tile(board)
                        score += gained_score
                        moves += 1
                game_over = is_game_over(board)
                
        # Draw the game state
        draw_board(screen, board, score, moves, game_over)
        pygame.display.flip()

if __name__ == "__main__":
    main()
