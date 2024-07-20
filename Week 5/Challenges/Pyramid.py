from graphics import Canvas
import random

CANVAS_WIDTH = 600   # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30       # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base
ROW_1_X_START_POINT = (CANVAS_WIDTH - (BRICKS_IN_BASE * BRICK_WIDTH)) // 2



def draw_rectangles(canvas, start_x, start_y, i):
    for j in range(BRICKS_IN_BASE - i):
        x1 = start_x + BRICK_WIDTH * j
        y1 = start_y
        x2 = x1 + BRICK_WIDTH
        y2 = y1 + BRICK_HEIGHT 
        canvas.create_rectangle(x1, y1, x2, y2, "yellow", "black")


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range(BRICKS_IN_BASE):
        draw_rectangles(canvas, (CANVAS_WIDTH - (BRICKS_IN_BASE* BRICK_WIDTH)) // 2 + (0.5 * BRICK_WIDTH * i), CANVAS_HEIGHT - (BRICK_HEIGHT * (i + 1)), i)

"""
        for j in range(BRICKS_IN_BASE):
            draw_rectangles(canvas, (CANVAS_WIDTH - (BRICKS_IN_BASE* BRICK_WIDTH)) // 2 + (0.5 * BRICK_WIDTH * i), CANVAS_HEIGHT - (BRICK_HEIGHT * (i + 1)))
            draw_rectangles(canvas, (CANVAS_WIDTH - (BRICKS_IN_BASE* BRICK_WIDTH)) // 2 + (BRICK_WIDTH * j), CANVAS_HEIGHT - BRICK_HEIGHT)
"""
    # draw remaining rectan

if __name__ == '__main__':
    main()