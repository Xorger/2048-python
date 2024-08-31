# Simple clone of 2048

import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()

SCREEN_SIZE: int = 500
try:
    TILE_SIZE: int = int(SCREEN_SIZE / 4)
except TypeError:
    print("SCREEN_SIZE must be integer multiple of 4")

tile_font = pygame.font.Font("clear-sans/ClearSans-Bold.ttf", 80)

# Create a class for the number tiles
class Tile(pygame.sprite.Sprite):
    def __init__(self, val):
        super(Tile, self).__init__()
        # Create and fill a Surface for tiles
        self.surf = pygame.Surface([TILE_SIZE, TILE_SIZE])
        self.surf.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0,255)))
        self.text = tile_font.render(f"{val}", True, (255, 255, 255))
        self.surf.blit(self.text, self.text.get_rect(center = self.surf.get_rect().center))

    def pos(self, row: int, column: int) -> tuple[int, int]:
        y: int = TILE_SIZE * row
        x: int = TILE_SIZE * column
        return (x, y)
def main():
    # Set up the drawing window
    screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
    # Create gameboard
    gameboard: list[list[int]] = [[0 for i in range(4)] for j in range(4)]
    gameboard[random.randint(0, 3)][random.randint(0, 3)] = 2
    # Create a list of tiles
    tiles: list[list[Tile]] = [[Tile(gameboard[i][j]) for i in range(4)] for j in range(4)]
    # Run until the user asks to quit
    running = True
    num_tiles: int = 0
    while running:

        # Detect the QUIT signal and button presses
        for event in pygame.event.get():
            if event.type == QUIT or event.type == K_ESCAPE:
                running = False
            if event.type == KEYDOWN:
                if event.type == K_UP:
                    #Move all non-zero elements up until they hit another non-zero element
                    board_copy: list[list[int]] = gameboard
                    while True:
                        for i, row in enumerate(gameboard):
                            for j, column in enumerate(row):
                                if gameboard[i - 1][j] != 0 and i > 0 and column != 0:
                                    board_copy[i - 1][j] = column
                                else:
                                    num_tiles += 1
                        gameboard = board_copy
                        for i, tile_row in enumerate(tiles):

                            for j, tile in enumerate(tile_row):
                                if gameboard[i][j]:
                                    screen.blit(tile.surf, tile.pos(i, j))
                        if num_tiles == 16:
                            break
                elif event.type == K_DOWN:
                    pass
                elif event.type == K_LEFT:
                    pass
                elif event.type == K_RIGHT:
                    pass
        # Fill the background with white
        screen.fill((255, 255, 255))
        #Draw a grid
        drawGrid(screen)
        # Blit the tile object
        for i, tile_row in enumerate(tiles):

            for j, tile in enumerate(tile_row):
                if gameboard[i][j]:
                    screen.blit(tile.surf, tile.pos(i, j))

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


def drawGrid(surface) -> None:
    for x in range(SCREEN_SIZE // TILE_SIZE):
        for y in range(SCREEN_SIZE // TILE_SIZE):
            rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE,
                               TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(surface, (0,0,0), rect, 1)

if __name__ == "__main__":
    main()
