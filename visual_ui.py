# ---- FILE: visual_ui.py ----

import pygame
from cube import Cube
from ida_star_solver import ida_star

pygame.init()
size = 60  # size of each sticker
margin = 10
width = 12 * size + 8 * margin
height = 9 * size + 6 * margin
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rubik's Cube Visual Solver")

FONT = pygame.font.SysFont(None, 36)
COLORS = {
    'W': (255, 255, 255),
    'Y': (255, 255, 0),
    'R': (255, 0, 0),
    'O': (255, 165, 0),
    'G': (0, 255, 0),
    'B': (0, 0, 255),
}

FACE_POS = {
    'U': (3, 0), 'L': (0, 3), 'F': (3, 3), 'R': (6, 3), 'B': (9, 3), 'D': (3, 6)
}

def draw_cube(cube):
    win.fill((30, 30, 30))
    for face, (x0, y0) in FACE_POS.items():
        for i in range(3):
            for j in range(3):
                color = COLORS[cube.faces[face][i][j]]
                rect = pygame.Rect(
                    margin + (x0 + j) * (size + margin),
                    margin + (y0 + i) * (size + margin),
                    size, size)
                pygame.draw.rect(win, color, rect)
                pygame.draw.rect(win, (0, 0, 0), rect, 2)
    pygame.display.flip()

def show_text(text, y_offset=0):
    surf = FONT.render(text, True, (255, 255, 255))
    win.blit(surf, (20, height - 50 + y_offset))
    pygame.display.update()

def main():
    cube = Cube()
    draw_cube(cube)
    scrambling = ['U', 'R', "U'", 'L', 'D', "B'"]
    for mv in scrambling:
        cube.move(mv)
    draw_cube(cube)
    solving = False
    solved = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not solving and not solved:
                    solving = True
                    show_text("Solving...")
                    solution = ida_star(cube)
                    for mv in solution:
                        pygame.time.delay(300)
                        cube.move(mv)
                        draw_cube(cube)
                    show_text("Solved!")
                    solved = True

        pygame.time.Clock().tick(30)

if __name__ == "__main__":
    main()