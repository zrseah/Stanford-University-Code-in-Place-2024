from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    player = draw_player(canvas)
    goal = draw_goal(canvas)
    
    player_x = 0 
    player_y = 0
    direction = None

    while True:
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            direction = "left"
            print('left arrow pressed!')
        elif key == 'ArrowRight':
            direction = "right"
            print('right arrow pressed!')
        elif key == 'ArrowUp':
            direction = "up"
            print('up arrow pressed!')
        elif key == 'ArrowDown':
            direction = "down"
            print('down arrow pressed!')

        if direction:
            if direction == "left":
                player_x -= SIZE # move left
            elif direction == "right":
                player_x += SIZE # move right
            elif direction == "up":
                player_y -= SIZE # move up
            elif direction == "down":
                player_y += SIZE # move down 
            
            x_p = canvas.get_left_x(player)
            y_p = canvas.get_top_y(player)
            print(x_p, y_p)
            
            if x_p >= 0 and x_p < CANVAS_WIDTH and y_p >= 0 and y_p < CANVAS_HEIGHT:
                canvas.moveto(player, player_x, player_y)
                time.sleep(DELAY)

                overlap = check_coincidence(canvas, goal)
                if player in overlap:
                    canvas.delete(goal)
                    goal = draw_goal(canvas)
            else: 
                print("game over!")
                break
            
def check_coincidence(canvas, goal):
    x_g = canvas.get_left_x(goal)
    y_g = canvas.get_top_y(goal)
    overlap = canvas.find_overlapping(x_g, y_g, x_g + SIZE, y_g + SIZE)
    print("overlap:", overlap)
    return overlap


def draw_player(canvas):
    x1 = 0
    y1 = 0
    x2 = x1 + SIZE
    y2 = y1 + SIZE
    player = canvas.create_rectangle(x1, y1, x2, y2, "blue")
    return player

def draw_goal(canvas):
    x1_g = random.randint(0, CANVAS_WIDTH - SIZE) //  20 * 20
    y1_g = random.randint(0, CANVAS_HEIGHT - SIZE) //  20 * 20
    x2_g = x1_g + SIZE
    y2_g = y1_g + SIZE
    goal = canvas.create_rectangle(x1_g, y1_g, x2_g, y2_g, "salmon")
    return goal
        

if __name__ == '__main__':
    main()