# Barnabas Ravindranath 
# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
RIGHT = True
ball_pos = [0,0]
ball_vel = [0, 0]
speed = 1.1
Win = ""

           

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [random.randrange(120,240), -(random.randrange(60,180))] 
    else:
        ball_vel = [-(random.randrange(120,240)), -(random.randrange(60,180))]

# define event handlers
def new_game():
    spawn_ball(RIGHT)
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, Win  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = [0,0]
    paddle2_vel = [0,0]
    score1 = 0
    score2 = 0
    Win = ""
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, Win
    Reset = ""
                    
#Ball Collides with either the Left Wall (Respawn) or the Left Paddle
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):
        if paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] 
            ball_vel[0] = ball_vel[0] * speed
            ball_vel[1] = ball_vel[1] * speed
        else:
            score1 += 1
            spawn_ball(RIGHT)
#Ball Collides with either the Right Wall (Respawn) or the Right Paddl   
    if ball_pos[0] >= ((WIDTH - PAD_WIDTH) - BALL_RADIUS):  
        if paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0] * speed
            ball_vel[1] = ball_vel[1] * speed
        else:
            score2 += 1
            spawn_ball(False)
            
#Top Wall and Bottom Wall      
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White") 
        
    # update ball
    ball_pos[0] += ball_vel[0]/60
    ball_pos[1] += ball_vel[1]/60
   
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "red", "red")
    
    # update paddle's vertical position and keep paddle on the screen
    
    if paddle1_pos + paddle1_vel[1] >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel[1] <= HEIGHT - HALF_PAD_HEIGHT :
        paddle1_pos += paddle1_vel[1]
        
    if paddle2_pos + paddle2_vel[1] >= HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel[1] <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel[1]
    
#left Paddle
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "white")      
#right Paddle
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "white")
       
#First To Seven
    if score1 == 7:
        Win = "Player 1 Wins!!"
        Reset = "REMATCH?!"
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        
    elif score2 == 7:
        Win = "Player 2 Wins!!!"
        Reset = "REMATCH?!"
        ball_pos = [WIDTH / 2, HEIGHT / 2]

    # draw scores
    canvas.draw_text("Player 1",  [500, 30], 15, "White")
    canvas.draw_text("Player 2",  [50, 30], 15, "White")
    canvas.draw_text(str(score1), [380, 50], 50, "White")
    canvas.draw_text(str(score2), [200, 50], 50, "White")
    canvas.draw_text(str(Win), [150, 200], 50, "White")
    canvas.draw_text(str(Reset), [220, 300], 30, "White")

       
def keydown(key):
    global paddle1_vel, paddle2_vel
    #paddle 1
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] += 5
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] -= 5
        
    #Paddle 2    
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += 5
        
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= 5
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    #paddle 1
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] -= 5
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] += 5 
    
    #paddle 1 
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] -= 5
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] += 5 


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game", new_game, 200)
label1 = frame.add_label("", 200)
label1 = frame.add_label("Welecome To Pong!", 200)
label1 = frame.add_label("", 200)
label1 = frame.add_label("Here are the Rules:", 200)
label1 = frame.add_label("", 200)
label3 = frame.add_label('First Player to score 7 points wins!', 200)
label1 = frame.add_label("", 200)
label1 = frame.add_label("", 200)
label1 = frame.add_label("", 200)
label1 = frame.add_label("", 200)
label1 = frame.add_label("", 200)
label1 = frame.add_label("", 200)
label1 = frame.add_label("", 200)
label1 = frame.add_label("", 200)
label2 = frame.add_label("Controls:", 200)
label1 = frame.add_label("Player 1 use Arrow Keys Player 2 use 'W/S'",200)



# start frame
new_game()
frame.start()
