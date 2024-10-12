import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    mouse_position = (0, 0)
    drawing = False
    erase = False
    screen = pygame.display.set_mode((600, 800), 0, 32)
    screen.fill(WHITE)
    pygame.display.set_caption("ScratchBoard")

    last_pos = None

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if (drawing):
                    mouse_position = pygame.mouse.get_pos()
                    if last_pos is not None:
                        pygame.draw.line(screen, BLACK, last_pos, mouse_position, 1)
                    last_pos = mouse_position
                elif (erase):
                    mouse_position = pygame.mouse.get_pos()
                    if last_pos is not None:
                        pygame.draw.line(screen, WHITE, last_pos, mouse_position, 20)
                    last_pos = mouse_position
            elif event.type == MOUSEBUTTONUP:
                mouse_position = (0, 0)
                drawing = False
                last_pos = None
            elif event.type == MOUSEBUTTONDOWN:
                drawing = True
            elif event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_e:
                    erase = True
            elif event.type == pygame.KEYUP:
                erase = False
                last_pos = None


        pygame.display.update()

if __name__ == "__main__":
    main()