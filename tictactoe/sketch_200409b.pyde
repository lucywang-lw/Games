import random
#0-empty, 1-x, 2-O
grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 1 player-ai

grid_2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 2 players

turn = 2
turn_2 = 2

# 0 -> instructions, 1 -> 2 players, 2 -> ai, 3 ->over
mode = 0

# winner position -> to determine winning line
position = 10
position_y = 10

position_2 = 10
position_y2 = 10

# instruction page
rule = 0

def reset():
    global mode, turn, turn_2, grid, o, position, position_y, position2, position_y2, grid_2, rule

    #0-empty, 1-x, 2-O
    grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 1 player-ai

    grid_2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 2 players

    turn = 2
    turn_2 = 2

    # winner position -> to determine winning line
    position = 10
    position_y = 10

    position_2 = 10
    position_y2 = 10
    rule = 0


def setup():
    size(800, 600)

def draw():
    global mode, turn, grid, o, position, position_y, position2, position_y2, stop
    background(204, 204, 255)  # background colour

    if mode == 0:
        instructions()
        if rule == 1:
            rules()

    if mode == 1:
        background_()
        gameboard()
        end_screen()

        if winners_2() != None:
            background_()
            gameboard()
            draw_stroke_2()
            end_screen()

    strokeWeight(1)
    stroke(0, 0, 0)

    # ai mode -> 1 player
    if mode == 2:
        background_()
        gameboard_ai()
        end_screen()
        draw_Xs()
        draw_Os()
        if winners() != None:
            draw_stroke()

    strokeWeight(1)
    stroke(0, 0, 0)

    if mode == 3:
        end_screen()

    fill(0, 0, 0)
    # X(player) wins
    if winners() == 1:
        text("You win!", 630, 150)

    # O(computer) wins
    if winners() == 2:
        text("You lost :(", 630, 150)


def mousePressed():
    global turn, mode, rule

    # 2 players
    if mouseX < 600 and grid_2[mouseY / 200][mouseX / 200] == 0 and mode == 1:
        grid_2[mouseY / 200][mouseX / 200] = turn_2
        turns_2()

    # AI- MOUSE CLICKED - Xs
    if mouseX < 600 and turn == 1:
        turn = 2
        for n in range(3):
            if grid[n] == 0 and (mouseX > (n * 200) and mouseX < (n * 200 + 200)) and (mouseY > 0 and mouseY < 200):
                grid[n] = 1
        for n in (3, 4, 5):
            if grid[n] == 0 and (mouseX > ((n - 3) * 200) and mouseX < ((n - 3) * 200 + 200)) and (mouseY > 200 and mouseY < 400):
                grid[n] = 1
        for n in (6, 7, 8):
            if grid[n] == 0 and (mouseX > ((n - 6) * 200) and mouseX < ((n - 6) * 200 + 200)) and (mouseY > 400 and mouseY < 600):
                grid[n] = 1

    # instructions screen- 1 player or 2 players button
    if mode == 0:
        # 2 players
        if mouseX > 300 and mouseX < 500 and mouseY > 270 and mouseY < 340:
            mode = 1
        # 1 player-AI
        elif mouseX > 300 and mouseX < 500 and mouseY > 390 and mouseY < 460:
            mode = 2
        # rules     rect(650,450,60,60)
        elif mouseX > 650 and mouseX < 710 and mouseY > 450 and mouseY < 510:
            rule = 1

    if mode == 1:
        if mouseX > 650 and mouseX < 760 and mouseY > 300 and mouseY < 350:
            mode = 1
            reset()
        elif mouseX > 650 and mouseX < 760 and mouseY > 400 and mouseY < 450:
            mode = 0
            reset()

    if mode == 2:
        if mouseX > 650 and mouseX < 760 and mouseY > 300 and mouseY < 350:
            mode = 2
            reset()
        elif mouseX > 650 and mouseX < 760 and mouseY > 400 and mouseY < 450:
            mode = 0
            reset()

def rules():
    fill(0, 0, 0)
    textSize(15)
    text("The first player to get 3 of", 540, 300)
    text("her marks in a row (up, down,", 540, 330)
    text("across, or diagonally) is ", 540, 360)
    text("the winner", 540, 390)


def end_screen():
    global mode
    textSize(40)
    fill(204, 102, 153)
    if winners_2() == 1:
        textSize(40)
        text("X wins", 650, 150)
    elif winners_2() == 2:
        text("O wins", 650, 150)

    rect(650, 300, 110, 50)
    rect(650, 400, 110, 50)

    textSize(18)
    fill(0, 0, 0)
    text("Play again", 665, 330)
    text("Home", 680, 430)


def draw_stroke():
    stroke(255, 0, 0)
    fill(255, 0, 0)
            # winning line for horizontal
    if position == 0 or position == 3:
        rect(50, position * 66.66 + 100, 500, 7)
    elif position == 6:
        rect(50, position * 100 - 95, 500, 7)
    elif position_y == 0 or position_y == 1 or position_y == 2:
        rect(position_y * 200 + 95, 50, 7, 500)

    elif grid[0] == grid[4] == grid[8]:
        strokeWeight(7)
        line(50, 50, 550, 550)
    elif grid[2] == grid[4] == grid[6] != 0:
        strokeWeight(7)
        line(550, 50, 50, 550)

def draw_stroke_2():
    fill(0, 0, 255)
    stroke(0, 0, 255)
    if position_2 == 0 or position_2 == 1 or position_2 == 2:
        rect(50, position_2 * 200 + 100, 500, 7)
    elif position_y2 == 0 or position_y2 == 1 or position_y2 == 2:
        rect(position_y2 * 200 + 100, 50, 7, 500)

    elif grid_2[0][0] == grid_2[1][1] == grid_2[2][2] != 0:
        strokeWeight(7)
        line(50, 50, 550, 550)
    elif grid_2[0][2] == grid_2[1][1] == grid_2[2][0] != 0:
        strokeWeight(7)
        line(550, 50, 50, 550)

def winners_2():
    global position_2, position_y2, grid_2
    # horizontal
    for x in range(3):
        if grid_2[x][0] == grid_2[x][1] == grid_2[x][2] != 0:
            position_2 = x
            return grid_2[x][0]

     # vertical
    for y in range(3):
        if grid_2[0][y] == grid_2[1][y] == grid_2[2][y] != 0:
            position_y2 = y
            return grid_2[0][y]

    if grid_2[0][0] == grid_2[1][1] == grid_2[2][2] != 0:
        return grid_2[0][0]
    if grid_2[0][2] == grid_2[1][1] == grid_2[2][0] != 0:
        return grid_2[0][2]


def winners():
    global position, x, grid, position_y, stop
    # horizontal
    for x in (0, 3, 6):
        if grid[x] == grid[x + 1] == grid[x + 2] != 0:
            position = x
            return (grid[x])
        # vertical
    for x in (0, 1, 2):
        if grid[x] == grid[x + 3] == grid[x + 6] != 0:
            position_y = x
            return grid[x]

        # diagonal
    if grid[0] == grid[4] == grid[8] != 0:
        return grid[0]

    if grid[2] == grid[4] == grid[6] != 0:
        return grid[2]


def background_():
    # game board square
    fill(255, 255, 255)
    rect(0, 0, 600, 600)

    # lines
    for x in range(3):
        line(200 * x, 0, 200 * x, 600)
    for y in range(3):
        line(0, 200 * y, 600, 200 * y)


# 2 players
def gameboard():
    for y in range(9):
        if grid[y] == 2:
            if y == 0 or y == 1 or y == 2:
                circle(y * 200 + 100, 100, 150)
            elif y == 3 or y == 4 or y == 5:
                circle((y - 3) * 200 + 100, 300, 150)
            elif y == 6 or y == 7 or y == 8:
                circle((y - 6) * 200 + 100, 500, 150)

        elif grid[y] == 1:
            if y == 0 or y == 1 or y == 2:
                rect(y * 200, 0, 150, 150)
            elif y == 3 or y == 4 or y == 5:
                rect((y - 3) * 200, 200, 150, 150)
            elif y == 6 or y == 7 or y == 8:
                rect((y - 6) * 200, 400, 150, 150)


def instructions():
    textSize(70)
    fill(0, 0, 0)
    text("TIC TAC TOE", 170, 200)

    # 1/2 player(s) buttons
    fill(0, 0, 0)
    rect(300, 270, 200, 70)
    rect(300, 390, 200, 70)

    fill(200)
    textSize(35)
    text("2 Players", 330, 320)
    text("1 Player", 330, 440)

    fill(0, 0, 0)
    rect(650, 450, 60, 60)
    textSize(20)
    fill(255, 255, 255)
    text("Rules", 655, 485)

# 2 players
def gameboard():
    global ai
    for y in range(3):
        for x in range(3):
            if grid_2[y][x] == 1:
                line(x * 200, y * 200 + 200, x * 200 + 200, y * 200)
                line(x * 200, y * 200, x * 200 + 200, y * 200 + 200)

            elif grid_2[y][x] == 2:
                circle(x * 200 + 100, y * 200 + 100, 150)

# ai
def gameboard_ai():
    global turn, grid
    o = 2  # change to 2-> place circle there
    # computer's turn
    if turn == 2:
        for n in range(1):
            # choose random variable in list
            random_index = random.randrange(len(grid))
            if grid[random_index] == 0:  # if random variable is 0(empty)
                grid[random_index] = o  # turn random variable to 2

                turn = 1
                break
            else:
                pass

def draw_Xs():
    # place a X where a 1 is detected in grid[]
    for y in range(9):
        if grid[y] == 1:  # if any value==1 -> draw a X
            if y == 0 or y == 1 or y == 2:
                line(y * 200, 0, y * 200 + 200, 200)
                line(y * 200, 200, y * 200 + 200, 0)
            elif y == 3 or y == 4 or y == 5:
                line((y - 3) * 200, 200, (y - 3) * 200 + 200, 400)
                line((y - 3) * 200, 400, (y - 3) * 200 + 200, 200)
            elif y == 6 or y == 7 or y == 8:
                line((y - 6) * 200, 400, (y - 6) * 200 + 200, 600)
                line((y - 6) * 200, 600, (y - 6) * 200 + 200, 400)

def draw_Os():
    # place a circle where a 2 is detected in grid[]
    if winners() != 1:
        fill(255, 255, 255)
        for y in range(9):
            if grid[y] == 2:
                if y == 0 or y == 1 or y == 2:
                    circle(y * 200 + 100, 100, 150)
                elif y == 3 or y == 4 or y == 5:
                    circle((y - 3) * 200 + 100, 300, 150)
                elif y == 6 or y == 7 or y == 8:
                    circle((y - 6) * 200 + 100, 500, 150)


# turns for 2 players
def turns_2():
    # change turns
    global turn_2
    if turn_2 == 1:
        turn_2 = 2
    else:
        turn_2 = 1
