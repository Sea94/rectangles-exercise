import pygame
from pygame.locals import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
RED = (210, 75, 45)
BACKGROUND = (250, 250, 250)
SELECTION = (40, 225, 130)
GRAY = (55, 60, 65)

BLOCK_SIZE = 100


def have_collided(rects):
    """
    Checks if two rectangles overlap
    :param rects: list of two Rect objects
    :return: bool do rectangles overlap
    """
    l1_x = rects[0].x
    l1_y = rects[0].y
    r1_x = rects[0].x + rects[0].w
    r1_y = rects[0].y + rects[0].h

    l2_x = rects[1].x
    l2_y = rects[1].y
    r2_x = rects[1].x + rects[1].w
    r2_y = rects[1].y + rects[1].h

    if(l1_x >= r2_x) or (l2_x >= r1_x):
        return False

    if(l1_y >= r2_y) or (l2_y >= r1_y):
        return False

    return True


def shrink_left(rect, step=5):
    """
    Handle LEFT ARROW key event.
    Shrink the rectangle along x-axis preserving the center position.
    :param rect: Rect object
    :param step: step in pixels
    :return: Rect object with updated coordinates
    """
    if (rect.w - 2 * step > 10):
        rect.x += step
        rect.w -= 2 * step
        return rect
    else:
        return rect


def shrink_down(rect, step=5):
    """
    Handle DOWN ARROW key event.
    Shrink the rectangle along y-axis preserving the center position.
    :param rect: Rect object
    :param step: step in pixels
    :return: Rect object with updated coordinates
    """
    if (rect.h - 2 * step > 10):
        rect.y += step
        rect.h -= 2 * step
        return rect
    else:
        return rect


def grow_right(rect, step=5):
    """
    Handle DOWN ARROW key event.
    Grow the rectangle along x-axis preserving the center position.
    :param rect: Rect object
    :param step: step in pixels
    :return: Rect object with updated coordinates
    """
    rect.x -= step
    rect.w += 2 * step
    return rect


def grow_up(rect, step=5):
    """
    Handle UP ARROW key event.
    Grow the rectangle along y-axis preserving the center position.
    :param rect: Rect object
    :param step: step in pixels
    :return: Rect object with updated coordinates
    """
    rect.y -= step
    rect.h += 2 * step
    return rect


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Resizable and movable rectangles')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    rects = []
    keys_dir = {
        K_LEFT: shrink_left,
        K_RIGHT: grow_right,
        K_UP: grow_up,
        K_DOWN: shrink_down
    }

    rects.append(pygame.Rect(100, 150, 100, 100))
    rects.append(pygame.Rect(400, 150, 100, 100))

    selected = -1  # id of currently selected rectangle
    moving = -1  # id of currently moving rectangle
    collided = False

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rects[0].collidepoint(event.pos):
                        selected = 0
                        moving = 0
                    elif rects[1].collidepoint(event.pos):
                        selected = 1
                        moving = 1
                    else:
                        selected = -1

            elif event.type == pygame.MOUSEBUTTONUP:
                moving = -1

            elif event.type == MOUSEMOTION and (moving != -1):
                rects[moving].move_ip(event.rel)
                collided = have_collided(rects)

            elif event.type == KEYDOWN:
                if selected != -1:
                    if event.key in keys_dir:
                        rects[selected] = keys_dir[event.key](rects[selected])
                        collided = have_collided(rects)

        screen.fill(BACKGROUND)

        for r in rects:
            pygame.draw.rect(screen, GRAY, r)

        font = pygame.font.SysFont(None, 36)
        text = font.render('The rectangles are overlapping!', True, RED)
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, 30))

        if collided:
            screen.blit(text, text_rect)
            pygame.draw.rect(screen, RED, rects[0])
            pygame.draw.rect(screen, RED, rects[1])
        if selected != -1:
            pygame.draw.rect(screen, SELECTION, rects[selected], 2)

        pygame.display.flip()

    pygame.quit()