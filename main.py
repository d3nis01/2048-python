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

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
