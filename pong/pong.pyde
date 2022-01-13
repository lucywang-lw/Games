     #left paddle
left_y = 260
left_x = 50
    #right paddle
right_y = 260
right_x = 820
    
    # ball position
ball_x = 450
ball_y = 300
    # ball speed
dx = 5
dy = 5
    
    # right player score
rs = 0
        # left player score
ls = 0
mode="instructions"
mode_1=""

#keys
r_key=""
l_key=""

def reset():
    global left_y,left_x,right_y,right_x,ball_x,ball_y,dx,dy,rs,ls
     #left paddle
    left_y = 260
    left_x = 50
    #right paddle
    right_y = 260 
    right_x = 820
    
    # ball position
    ball_x = 450
    ball_y = 300
    # ball speed
    dx = 5
    dy = 5
    
    # right player score
    rs = 0
    # left player score
    ls = 0
    
def setup():
    size(900, 600)

def draw():
    global ball_x, ball_y, dx, dy, ls, rs,mode,l_key,r_key,left_y,right_y
    

    if mode=="instructions":
        background(0, 0, 0)
        textSize(50)
        fill(255,255,255)
        text("Pong",385,80)
        
        fill(255,215,51)
        rect(250,200,400,300)
        fill(0,0,0)
        textSize(17)  
        text("Right player: Control paddle with up",280,230)
        text("and down keys.",280,255)
        text("Left player: Control paddle with W",280,290)
        text("and S keys.",280,315)
        text("Earn points when your opponent misses.",280,345)
        text("Game ends at 10 points.", 280, 380)
        textSize(20)
        text("Press Space Bar to start game",300,450)    

    
    elif mode=="on":
    #move right paddle
        if r_key == "d":
            right_y += 4
        if r_key == "u":
            right_y -= 4
    # move left paddle
        if l_key=="s":
            left_y += 4
        if l_key=="w":
            left_y -= 4
    
    #detect if ball goes past paddle and score
        if ball_x > width:
            ls += 1  # score
            ball_x = 450
            ball_y = 300
            dx = -5  # go left
        if ball_x < 0:
            rs += 1
            ball_x = 450
            ball_y = 300
            dx = 5  # go right

    #collision detection
        if (ball_x+20) == right_x and ball_y > right_y and ball_y < right_y+90:
                dx = -5
    
        if (ball_x) == left_x+30 and ball_y > left_y and ball_y < left_y+90:
                dx = 5
    
        if ball_y > height - 30:
            dy -= 5
        if ball_y < 30:
            dy += 5
    
        #move ball
        ball_x += dx
        ball_y += dy
    
        if ls==10 or rs==10:
            mode="end"
    
        background(0, 0, 0)
    
        # paddles
        fill(255,215,51)
        rect(450,0,2,600) #line 
    
        rect(left_x, left_y, 20, 90)  # left
        rect(right_x, right_y, 20, 90)  # right
    
        # ball
        circle(ball_x, ball_y, 30)
    
        #title and score
        textSize(40)
        fill(255)
        text("Pong", 400, 60)
        
        textSize(32)
        text(ls, 70, 70)
        text(rs, 800, 70)
        
    elif mode=="end":
        fill(205,205,205)
        rect(300,130,300,300)
        fill(255,215,51)
        rect(400,300,100,50)
        
        fill(0,0,0)
        textSize(20)
        text("Again",425,330)
        fill(0,0,0)
        textSize(30)        
        if rs>ls:
            text("Right player wins", 330, 250)
        elif ls>rs:
            text("Left player wins", 330,250)

    
def keyReleased():
    global l_key,r_key
    
    if keyCode == DOWN:
        r_key=""
    if keyCode == UP:
        r_key=""
    # move left paddle
    if key == "s" or key == "S":
        l_key=""
    if key == "w" or key == "W":
        l_key=""

        
def keyPressed():
    global l_key,r_key, mode
    
    if mode=="instructions" and key==" ":
        mode="on"    

    # move right paddle
    if keyCode == DOWN:
        r_key="d"
    if keyCode == UP:
        r_key="u"
    # move left paddle
    if key == "s" or key == "S":
        l_key="s"
    if key == "w" or key == "W":
        l_key="w"


                
def mousePressed():
    global mode
    print(mouseX,mouseY)
    


    if mode=="end":
        if mouseX>400 and mouseX<500 and mouseY>300 and mouseY<350:
            mode="on"
            reset()
            

    
