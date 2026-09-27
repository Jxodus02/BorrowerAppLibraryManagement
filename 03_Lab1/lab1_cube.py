import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# Vertices of the cube (Step 14 table)
vertices = (
    (1, 1, 1),     # 0
    (1, 1, -1),    # 1
    (1, -1, -1),   # 2
    (1, -1, 1),    # 3
    (-1, 1, 1),    # 4
    (-1, -1, -1),  # 5
    (-1, -1, 1),   # 6
    (-1, 1, -1),   # 7
)

# Edges of the cube (Step 15 table)
edges = (
    (0, 1),  # A
    (1, 2),  # B
    (2, 3),  # C
    (3, 0),  # D
    (4, 7),  # E
    (7, 5),  # F
    (5, 6),  # G
    (6, 4),  # H
    (3, 6),  # I
    (0, 4),  # J
    (2, 5),  # K
    (1, 7),  # L
)


def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("03 Lab 1 - Your Full Name")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(15)


main()
