from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    x1 = 0
    y1 = 0
    x2 = CANVAS_WIDTH
    y2 = CANVAS_HEIGHT/2

    canvas.create_rectangle(x1, y1, x2, y2, "red")
    

if __name__ == '__main__':
    main()