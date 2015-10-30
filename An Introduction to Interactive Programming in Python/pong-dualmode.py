import simplegui
import random

#globals
WIDTH = 800
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
opt_pos=[0,0]
ball_pos = [WIDTH/2,HEIGHT/2]
ball_vel = [-random.randrange(60, 180)/60,random.randrange(120, 240)/60]
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
player1="PLAYER 1 "
player2="PLAYER 2 "
game_mode=0
# helper function that moves a ball, returns a position vector and a velocity vector
# if right is True, move to the right, else move to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel[1] = -random.randrange(60, 180)/60
    if right == True:
        ball_vel[0] = random.randrange(120, 240)/60
    else:
        ball_vel[0] = -random.randrange(120, 240)/60
    pass

# defining event Handlers
##
##
##computer play
def tick():
    global paddle1_vel,paddle1_pos,ball_pos
    if ball_pos[0]<WIDTH/3:
        paddle1_pos=random.randrange(ball_pos[1]-25,ball_pos[1]+25)
    
    
    
def click(pos):
    global opt_pos,game_mode
    opt_pos = list(pos)
    if game_mode==0:
        if opt_pos[0]>490 and opt_pos[0]<700 and opt_pos[1]>270 and opt_pos[1]<310:
            play2()
        if opt_pos[0]>90 and opt_pos[0]<310 and opt_pos[1]>270 and opt_pos[1]<310:
            play1()
    elif game_mode==4:
        if opt_pos[0]>240 and opt_pos[0]<450 and opt_pos[1]>280 and opt_pos[1]<340:
            game_mode=0
def play2():
    global game_mode
    game_mode=2
    init()
def game_intro(c):
    c.draw_text("WELCOME TO PONG",(250,HEIGHT/2),36,"RED")
    c.draw_text("VERSION 1.0",(2,20),20,"black")
    c.draw_text("CREATED BY: NISHANT SHRESHTH",(450,20),20,"RED")
    c.draw_text("SINGLE PLAYER",(100,300),30,"RED")
    c.draw_text("DOUBLE PLAYER",(500,300),30,"RED")
    c.draw_text("##FOR SINGLE PLAYER- USE UP AND DOWN ARROW KEY",(2,380),16,"GREEN")
    c.draw_text("##FOR DOUBLE PLAYER: PLAYER 1 USE 'W' AND 'S' KEY and PLAYER 2 USE UP AND DOWN ARROW KEY",(2,350),16,"GREEN")
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    ball_init(0 == random.randrange(0,11) % 2)
    pass
def drawend(c):
    msg=player1
    if score2 > score1:
        msg=player2
    c.draw_text(msg+" WON !!!",(200,HEIGHT/2),40,"RED")
    c.draw_text("WANNA PLAY AGAIN",(250,300),28,"RED")
        
def draw(c):
    global game_mode
    if game_mode==0:
        game_intro(c)
    elif game_mode==1:
        drawplay1(c)
    elif game_mode==2:
        drawplay2(c)
    elif game_mode==4:
        drawend(c)
def play1():
    global game_mode,paddle1_vel,player1,player2
    paddle1_vel=5 
    game_mode=1
    timer.start()
    player1="COMPUTER "
    player2="CONGO YOU "
    init()
def drawplay1(c):
    global score1, score2, paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos, ball_pos, ball_vel,game_mode
    if paddle2_pos < (HALF_PAD_HEIGHT) and paddle2_vel < 0:
        paddle2_vel = 0
    if paddle2_pos > (HEIGHT - (HALF_PAD_HEIGHT)) and paddle2_vel > 0:
        paddle2_vel = 0    
    paddle2_pos += paddle2_vel        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "black")
    c.draw_circle([WIDTH/2,HEIGHT/2],30,2,"black")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # draw paddles
    c.draw_polygon([(0, paddle1_pos-HALF_PAD_HEIGHT), (0, paddle1_pos+HALF_PAD_HEIGHT), (PAD_WIDTH-2, paddle1_pos+HALF_PAD_HEIGHT),(PAD_WIDTH-2,paddle1_pos-HALF_PAD_HEIGHT)], PAD_WIDTH-1, "RED","RED")
    c.draw_polygon([(WIDTH, paddle2_pos-HALF_PAD_HEIGHT), (WIDTH, paddle2_pos+HALF_PAD_HEIGHT), (WIDTH-PAD_WIDTH+2, paddle2_pos+HALF_PAD_HEIGHT),(WIDTH-PAD_WIDTH+2,paddle2_pos-HALF_PAD_HEIGHT)], PAD_WIDTH-1, "GREEN","GREEN")
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS) or ball_pos[1] <= (BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):
        if ball_pos[1] < (paddle1_pos - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle1_pos + HALF_PAD_HEIGHT):
            ball_init(True)
            score2 += 1
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
            
    if  ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        if ball_pos[1] < (paddle2_pos - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle2_pos + HALF_PAD_HEIGHT):
            ball_init(False)
            score1 += 1
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
    if score1==5 or score2==5:
        game_mode=4
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "yellow")
    c.draw_text("COMPUTER: "+str(score1), (100, 50), 36, "Red")
    c.draw_text("YOU: "+str(score2), (500, 50), 36, "GREEN")
def drawplay2(c):
    
    global game_mode,score1, score2, paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos < (HALF_PAD_HEIGHT) and paddle1_vel < 0:
        paddle1_vel = 0
    if paddle2_pos < (HALF_PAD_HEIGHT) and paddle2_vel < 0:
        paddle2_vel = 0
    if paddle1_pos > (HEIGHT - (HALF_PAD_HEIGHT)) and paddle1_vel > 0:
        paddle1_vel = 0
    if paddle2_pos > (HEIGHT - (HALF_PAD_HEIGHT)) and paddle2_vel > 0:
        paddle2_vel = 0    
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "black")
    c.draw_circle([WIDTH/2,HEIGHT/2],30,2,"black")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # draw paddles
    c.draw_polygon([(0, paddle1_pos-HALF_PAD_HEIGHT), (0, paddle1_pos+HALF_PAD_HEIGHT), (PAD_WIDTH-2, paddle1_pos+HALF_PAD_HEIGHT),(PAD_WIDTH-2,paddle1_pos-HALF_PAD_HEIGHT)], PAD_WIDTH-1, "RED","RED")
    c.draw_polygon([(WIDTH, paddle2_pos-HALF_PAD_HEIGHT), (WIDTH, paddle2_pos+HALF_PAD_HEIGHT), (WIDTH-PAD_WIDTH+2, paddle2_pos+HALF_PAD_HEIGHT),(WIDTH-PAD_WIDTH+2,paddle2_pos-HALF_PAD_HEIGHT)], PAD_WIDTH-1, "GREEN","GREEN")
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS) or ball_pos[1] <= (BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):
        if ball_pos[1] < (paddle1_pos - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle1_pos + HALF_PAD_HEIGHT):
            ball_init(True)
            score2 += 1
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
            
    if  ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        if ball_pos[1] < (paddle2_pos - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle2_pos + HALF_PAD_HEIGHT):
            ball_init(False)
            score1 += 1
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
    if score1==5 or score2==5:
        game_mode=4
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "yellow")
    c.draw_text("PLAYER 1: "+str(score1), (100, 50), 36, "Red")
    c.draw_text("PLAYER 2: "+str(score2), (500, 50), 36, "GREEN")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if game_mode==1:
        if key == simplegui.KEY_MAP['up']:
            paddle2_vel = -4
        elif key == simplegui.KEY_MAP['down']:
            paddle2_vel = 4  
    else:
        if key == simplegui.KEY_MAP['w']:
            paddle1_vel = -4
        elif key == simplegui.KEY_MAP['s']:
            paddle1_vel = 4
        elif key == simplegui.KEY_MAP['up']:
            paddle2_vel = -4
        elif key == simplegui.KEY_MAP['down']:
            paddle2_vel = 4
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if game_mode==1:
         if key == simplegui.KEY_MAP['up']:
             paddle2_vel = 0
         elif key == simplegui.KEY_MAP['down']:
             paddle2_vel = 0
    else:
        if key == simplegui.KEY_MAP['w']:
            paddle1_vel = 0
        elif key == simplegui.KEY_MAP['s']:
            paddle1_vel = 0
        elif key == simplegui.KEY_MAP['up']:
            paddle2_vel = 0
        elif key == simplegui.KEY_MAP['down']:
            paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background("White")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)
frame.set_mouseclick_handler(click)
timer=simplegui.create_timer(200,tick)

# start frame
frame.start()
