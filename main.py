# Simple clone of 2048

import pygame
import random
pygame.init()

SCREEN_SIZE = 500
try:
    TILE_SIZE = int(SCREEN_SIZE / 4)
except TypeError:
    print("SCREEN_SIZE must be integer multiple of 4")
# Create a class for the number tiles
class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super(Tile, self).__init__()
        # Create and fill a Surface for tiles
        self.surf = pygame.Surface([TILE_SIZE, TILE_SIZE])
        self.surf.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0,255)))

    def pos(self, row: int, column: int) -> tuple[int, int]:  
        y = TILE_SIZE * row
        x = TILE_SIZE * column
        return (x, y)
def main():
    # Set up the drawing window
    screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
    
    # Create gameboard
    gameboard = [[0 for i in range(4)] for j in range(4)]

    # Create a list of tiles
    tiles = [[Tile() for i in range(4)] for j in range(4)]
    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))
        # Blit the tile object
        for i, tile_row in enumerate(tiles):

            for j, tile in enumerate(tile_row):
                screen.blit(tile.surf, tile.pos(i, j))

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
    main()
