player=int(input("Would you like to play as Player 1 or Player 2: "))
if player==1:
    input("Player 1: Are you ready to position your fleet?  Press enter to begin!")
else:
    input("Player 2: Are you ready to position your fleet?  Press enter to begin!")
print("  ", end='')
for i in range(10):
    print(i, end=' ')
print()
for k in range(10):
    print(k, "_ "*10)
board_pos=[["_" for j in range(10)] for i in range(10)]
def fleetpos(x_pos,y_pos,orientation,fleet_length):
    global board_pos
    if orientation=="v":
        for k in range(fleet_length):
            if y_pos+fleet_length<10:
                board_pos[y_pos+k][x_pos]="B"
            else:
                print("Please enter proper coordinates.")
                xn,yn=[int(x) for x in input("Please enter the position for the top-left location of the boat.  Use the form x,y (e.g., 1,3): ").split(",")]
                return fleetpos(xn,yn,o,fleet_length)
    elif orientation=="h":
        for l in range(fleet_length):
            if x_pos+fleet_length<10:
                board_pos[y_pos][x_pos+l]="B"
            else:
                print("Please enter proper coordinates.")
                xn,yn=[int(x) for x in input("Please enter the position for the top-left location of the boat.  Use the form x,y (e.g., 1,3): ").split(",")]
                return fleetpos(xn,yn,o,fleet_length)
            
    print("  ", end='')
    for m in range(10):
        print(m, end=' ')
    print()
    n=0
    for row in board_pos:
        print(n, end=' ')
        for elem in row:
            print(elem, end=' ')
        n+=1
        print()
print("You need to position a Aircraft Carrier of length 5 on the board above.")
o=input("Would you like to use a vertical or horizontal orientation? (v/h) ")
x,y=[int(x) for x in input("Please enter the position for the top-left location of the boat.  Use the form x,y (e.g., 1,3): ").split(",")]
fleetpos(x,y,o,5)

print("You need to position a Battle Ship of length 4 on the board above.")
o=input("Would you like to use a vertical or horizontal orientation? (v/h) ")
x1,y1=[int(x) for x in input("Please enter the position for the top-left location of the boat.  Use the form x,y (e.g., 1,3): ").split(",")]
fleetpos(x1,y1,o,4)                   

print("You need to position a Submarine of length 3 on the board above.")
o=input("Would you like to use a vertical or horizontal orientation? (v/h) ")
x2,y2=[int(x) for x in input("Please enter the position for the top-left location of the boat.  Use the form x,y (e.g., 1,3): ").split(",")]        
fleetpos(x2,y2,o,3)

print("You need to position a Destroyer of length 3 on the board above.")
o=input("Would you like to use a vertical or horizontal orientation? (v/h) ")
x3,y3=[int(x) for x in input("Please enter the position for the top-left location of the boat.  Use the form x,y (e.g., 1,3): ").split(",")]
fleetpos(x3,y3,o,3)

print("You need to position a Patrol Boat of length 2 on the board above.")
o=input("Would you like to use a vertical or horizontal orientation? (v/h) ")
x4,y4=[int(x) for x in input("Please enter the position for the top-left location of the boat.  Use the form x,y (e.g., 1,3): ").split(",")]
fleetpos(x4,y4,o,2)




comp_board_pos=[["_" for j in range(10)]for i in range(10)]
comp_board_pos_playerview=[["_" for j in range(10)]for i in range(10)]
import random
def compfleetpos(fleet_length):
    x_pos=0
    y_pos=0
    orientation=random.choice(["v","h"])
    if orientation=="v":
        x_pos=random.randrange(0,10)
        for pos in range(10):
            y_random=random.randrange(0,10)
            if y_random+fleet_length<10:
                y_random=y_pos
    elif orientation=="h":
        y_pos=random.randrange(0,10)
        for pos in range(10):
            x_random=random.randrange(0,10)
            if x_random+fleet_length<10:
                x_random=x_pos
    
    
    global comp_board_pos
    if orientation=="v":
        for k in range(fleet_length):
            if y_pos+fleet_length<10:
                comp_board_pos[y_pos+k][x_pos]="B"
    elif orientation=="h":
        for l in range(fleet_length):
            if x_pos+fleet_length<10:
                comp_board_pos[y_pos][x_pos+l]="B"

def playerboardview():
    
    
    global board_pos
    print("Your board: ")
    print("  ", end='')
    for m in range(10):
        print(m, end=' ')
    print()
    n=0
    for row in board_pos:
        print(n, end=' ')
        for elem in row:
            print(elem, end=' ')
        n+=1
        print()
def compboardview():
    global comp_board_pos_playerview
    print("Your view of Computer's board: ")
    print("  ", end='')
    for m in range(10):
        print(m, end=' ')
    print()
    n=0
    for row in comp_board_pos_playerview:
        print(n, end=' ')
        for elem in row:
            print(elem, end=' ')
        n+=1
        print()
phits=0
pmiss=0
def player_check(x_hit,y_hit):
    global comp_board_pos_playerview, comp_board_pos, phits, pmiss
    if comp_board_pos[y_hit][x_hit]=="B":
        print("It was a hit.")
        comp_board_pos[y_hit][x_hit]="X"
        comp_board_pos_playerview[y_hit][x_hit]="X"
        phits+=1
    else:
        comp_board_pos[y_hit][x_hit]="O"
        comp_board_pos_playerview[y_hit][x_hit]="O"
        print("You missed.")
        pmiss+=1
    print("No. of hits are", phits, "and no. of miss by you are", pmiss )
    playerboardview()
    compboardview()
chits=0
cmiss=0
def comp_check(x_hit,y_hit):
    print("Its Computer's Turn.")
    global board_pos, chits, cmiss
    if board_pos[y_hit][x_hit]=="B":
        print("It was a hit.")
        board_pos[y_hit][x_hit]="X"
        chits+=1
    else:
        board_pos[y_hit][x_hit]="O"
        print("Computer missed.")
        cmiss+=1
    print("No. of hits are", chits, "and no. of miss by computer are", cmiss )
    playerboardview()
    compboardview()
def playerfirst():
    x_cturn=random.randrange(0,10)
    y_cturn=random.randrange(0,10)
    comp_check(x_cturn,y_cturn)
    print("It's your turn. Select a coordinate(form of x,y): ", end=' ')
    x_turn,y_turn=int(input().split(','))
    player_check(x_turn,y_turn)
def playersecond():
    print("It's your turn. Select a coordinate(form of x,y): ", end=' ')
    x_turn,y_turn=int(input().split(','))
    player_check(x_turn,y_turn)
    x_cturn=random.randrange(0,10)
    y_cturn=random.randrange(0,10)
    comp_check(x_cturn,y_cturn)
print("Now the Computer will place its fleet.")
compfleetpos(5)
compfleetpos(4)
compfleetpos(3)
compfleetpos(3)
compfleetpos(2)
print("Computer has positioned its fleet.")
playerboardview()
compboardview()
if player==1:
    print("It's your turn first. Select a coordinate(form of x,y): ", end=' ')
    x_turn,y_turn=[int(x) for x in input().split(',')]
    player_check(x_turn,y_turn)
    while True:
        if phits==16:
            print("You have Won the game. Congrats!")
            break
        elif chits==16:
            print("Computer has won the round.")
            break
        elif phits<16:
            playerfirst()
            
            
            
else:
    x_cturn=random.range(0,10)
    y_cturn=random.range(0,10)
    comp_check(x_cturn,y_cturn)
    while True: 
        if phits==16:
            print("You have Won the game. Congrats!")
            break
        elif chits==16:
            print("Computer has won the round.")
            break
        elif phits<16:
            playersecond()
        
    
    


