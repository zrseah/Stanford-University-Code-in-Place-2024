"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from graphics import Canvas

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
FIRST_LINE_LEFT_X = 50
FIRST_LINE_TOP_Y = 50
FONT_SIZE = 24

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_text(FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y,
    "An old silent pond...",
    color = "blue",
    font = "Courier",
    font_size = FONT_SIZE)

    canvas.create_text(FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y + FONT_SIZE,
    "A frog jumps into the pond,",
    color = "blue",
    font = "Courier",
    font_size = FONT_SIZE)

    canvas.create_text(FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y + 2 * FONT_SIZE,
    "splash! Silence again.",
    color = "blue",
    font = "Courier",
    font_size = FONT_SIZE)

    
    
    

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()