"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Create mirror line
    canvas.create_line(
        CANVAS_WIDTH // 2, 
        0, 
        CANVAS_WIDTH // 2, 
        CANVAS_HEIGHT)
    
    # Create red rectangle
    rect_left_x = 20
    rect_top_y = 50
    rect_width = 100
    rect_height = 200
    canvas.create_rectangle(
        rect_left_x, 
        rect_top_y, 
        rect_left_x + rect_width, 
        rect_top_y + rect_height, 
        'red')
    
    # Create blue rectangle 
    DIST_BTW_RHS_RED_REC_AND_MIRROR = (CANVAS_WIDTH // 2) - (rect_left_x + rect_width)
    x1 = (CANVAS_WIDTH // 2) + DIST_BTW_RHS_RED_REC_AND_MIRROR
    y1 = rect_top_y
    x2 = x1 + rect_width
    y2 = rect_top_y + rect_height

    canvas.create_rectangle(x1, y1, x2, y2, "blue")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()