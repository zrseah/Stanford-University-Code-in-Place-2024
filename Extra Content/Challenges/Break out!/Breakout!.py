from graphics import Canvas
import time
import random
import math

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 600
PADDLE_Y = CANVAS_HEIGHT - 30
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
BALL_RADIUS = 10

BRICK_GAP = 5
BRICK_WIDTH = (CANVAS_WIDTH - BRICK_GAP*9) / 10
BRICK_HEIGHT = 10
 
BB_START_X = (CANVAS_WIDTH - 2 * BALL_RADIUS)/2 
BB_START_Y = (CANVAS_HEIGHT - 2* BALL_RADIUS)/2  

VELOCITY =  random.randint(1, 5)

DELAY = 0.001

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    bricks = draw_bricks(canvas)
    paddle, py1 = draw_paddle(canvas)
    bouncing_ball(canvas, paddle, py1, bricks)

def bouncing_ball(canvas, paddle, py1, bricks):
    bbx1 = BB_START_X
    bby1 = BB_START_Y
    bbx2 = bbx1 + 2 * BALL_RADIUS
    bby2 = bby1 + 2 * BALL_RADIUS
    ball = canvas.create_oval(bbx1, bby1, bbx2, bby2, "black")

    change_x = VELOCITY
    change_y = VELOCITY
    penalty = 0
    max_panelty = 4

    while penalty < max_panelty:
        if len(bricks) > 0: 
            mouse_x = canvas.get_mouse_x()

            if bbx1 <= 0 or bbx1 +  2 * BALL_RADIUS > CANVAS_WIDTH:
                change_x = -change_x
            
            if bby1 <= 0:
                change_y = -change_y
            
            if bby1 > CANVAS_HEIGHT:
                change_y = -change_y
                penalty += 1 
                print("Penalty:", penalty)

            p_collision = paddle_collision(canvas, mouse_x, py1)
            if ball in p_collision:
                change_y = -change_y
            
            b_collision = ball_collision(canvas, bbx1, bby1)
            for brick in b_collision:
                if brick!= ball and brick!= paddle: # ensure that object is not a paddle or ball
                    if brick in bricks: # ensure that brick is in bricks 
                        change_y = -change_y
                        canvas.delete(brick)
                        bricks.remove(brick)

            bbx1 += change_x
            bby1 += change_y

            # Move the ball
            canvas.moveto(ball, bbx1, bby1)

            # Move the paddle
            canvas.moveto(paddle, mouse_x, py1)

            time.sleep(DELAY)
        else:
            print("Congratulations! You have won!")
            break
    else:
        print("Game Over")

def ball_collision(canvas, bbx1, bby1):
    b_collision = canvas.find_overlapping(bbx1, bby1, bbx1 + 2 * BALL_RADIUS, bby1 + 2 * BALL_RADIUS)
    return b_collision

def paddle_collision(canvas, mouse_x, py1):
    p_collision = canvas.find_overlapping(mouse_x, py1, mouse_x + PADDLE_WIDTH, py1 + PADDLE_HEIGHT)
    return p_collision
        
def draw_paddle(canvas):
    px1 = CANVAS_WIDTH/2 - PADDLE_WIDTH/2
    py1 = PADDLE_Y
    px2 = px1 + PADDLE_WIDTH
    py2 = py1 + PADDLE_HEIGHT
    paddle = canvas.create_rectangle(px1, py1, px2, py2, "black")
    
    return paddle, py1 

def draw_bricks(canvas):
    start_x  = (CANVAS_WIDTH - (10 * BRICK_WIDTH + 9 * BRICK_GAP))/ 2
    start_y = 50

    bricks = []
   
    for i in range(10):
        for u in range(2):
            bx1 = start_x + i * (BRICK_WIDTH + BRICK_GAP)
            by1 = start_y + u * (BRICK_HEIGHT + BRICK_GAP)
            bx2 = bx1 + BRICK_WIDTH
            by2 = by1 + BRICK_HEIGHT
            brick = canvas.create_rectangle(bx1, by1, bx2, by2, "red")
            bricks.append(brick) 

    for i in range(10):
        for u in range(2):
            bx1 = start_x + i * (BRICK_WIDTH + BRICK_GAP)
            by1 = start_y + 2 * (BRICK_HEIGHT + BRICK_GAP) + u * (BRICK_HEIGHT + BRICK_GAP)
            bx2 = bx1 + BRICK_WIDTH
            by2 = by1 + BRICK_HEIGHT
            brick = canvas.create_rectangle(bx1, by1, bx2, by2, "orange")
            bricks.append(brick) 

    for i in range(10):
        for u in range(2):
            bx1 = start_x + i * (BRICK_WIDTH + BRICK_GAP)
            by1 = start_y + 4 * (BRICK_HEIGHT + BRICK_GAP) + u * (BRICK_HEIGHT + BRICK_GAP)
            bx2 = bx1 + BRICK_WIDTH
            by2 = by1 + BRICK_HEIGHT
            brick = canvas.create_rectangle(bx1, by1, bx2, by2, "yellow")
            bricks.append(brick)

    for i in range(10):
        for u in range(2):
            bx1 = start_x + i * (BRICK_WIDTH + BRICK_GAP)
            by1 = start_y + 6 * (BRICK_HEIGHT + BRICK_GAP) + u * (BRICK_HEIGHT + BRICK_GAP)
            bx2 = bx1 + BRICK_WIDTH
            by2 = by1 + BRICK_HEIGHT
            brick = canvas.create_rectangle(bx1, by1, bx2, by2, "green")
            bricks.append(brick)

    for i in range(10):
        for u in range(2):
            bx1 = start_x + i * (BRICK_WIDTH + BRICK_GAP)
            by1 = start_y + 8 * (BRICK_HEIGHT + BRICK_GAP) + u * (BRICK_HEIGHT + BRICK_GAP)
            bx2 = bx1 + BRICK_WIDTH
            by2 = by1 + BRICK_HEIGHT
            brick = canvas.create_rectangle(bx1, by1, bx2, by2, "cyan")
            bricks.append(brick)

    return bricks 

if __name__ == '__main__':
    main()