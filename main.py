import pygame
import random
from moves import *
import sys

GRID_SIZE = 4
TILE_SIZE = 100
TILE_MARGIN = 10
INFO_HEIGHT = 100
SCREEN_SIZE = GRID_SIZE * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN
WINDOW_HEIGHT = SCREEN_SIZE + INFO_HEIGHT

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

pygame.font.init()
FONT = pygame.font.Font(None, 40)
INFO_FONT = pygame.font.Font(None, 50)
GAME_OVER_FONT = pygame.font.Font(None, 60)


def init_game():
    board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    return board

def add_new_tile(board):
    empty_tiles = [(row, column) for row in range(GRID_SIZE) for column in range(GRID_SIZE) if board[row][column] == 0]
    if empty_tiles:
        r, c = random.choice(empty_tiles)
        board[r][c] = 2 if random.random() < 0.9 else 4
        
def is_game_over(board):
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            if board[row][column] == 0:
                return False
            if row < GRID_SIZE - 1 and board[row][column] == board[row + 1][column]:
                return False
            if column < GRID_SIZE - 1 and board[row][column] == board[row][column + 1]:
                return False
    return True

def get_highest_tile(board):
    return max(max(row) for row in board)


def draw_board(screen, board, score, moves, game_over=False):
    screen.fill((187, 173, 160))

    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            value = board[r][c]
            color = COLORS.get(value, (60, 58, 50))
            rect = pygame.Rect(
                c * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN,
                r * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN + INFO_HEIGHT,
                TILE_SIZE, TILE_SIZE
            )
            pygame.draw.rect(screen, color, rect)
            if value:
                text = FONT.render(str(value), True, (119, 110, 101))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

    highest_tile = get_highest_tile(board)

    score_text = INFO_FONT.render(f"Score: {score}", True, (255, 255, 255))
    moves_text = INFO_FONT.render(f"Moves: {moves}", True, (255, 255, 255))
    highest_text = INFO_FONT.render(f"Highest Tile: {highest_tile}", True, (255, 255, 255))

    screen.blit(score_text, (20, 20))  
    screen.blit(moves_text, (SCREEN_SIZE - 200, 20)) 
    screen.blit(highest_text, (20, 60))

    if game_over:
        game_over_text = GAME_OVER_FONT.render("Game Over!", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(
            center=(SCREEN_SIZE // 2, (WINDOW_HEIGHT + INFO_HEIGHT) // 2)
        )
        screen.blit(game_over_text, text_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, WINDOW_HEIGHT))
    pygame.display.set_caption("2048")
    board = init_game()
    score = 0
    moves = 0
    add_new_tile(board)
    add_new_tile(board)
    clock = pygame.time.Clock()
    
    game_over = False


    while True:
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
                
        draw_board(screen, board, score, moves, game_over)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()