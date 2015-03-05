#Bowling game source code - BBC Technical exercise - Luke Unsworth 19/02/15
#
# TODO:
#   - Write scoring "engine"
#       - Function?
#   - Create class of "Frame".
#       - Int Shot1
#       - Int Shot2
#       - Int Total (because of strikes and stuff)
#   - Create class of "Player"
#       - Array of 10 "Frame".
#       - String "PlayerName"
#       - Int "PlayerScore"
#
#   Create Dict of players.
#   
#   - Testing:
#       - MAKE SURE TO USE THE "XXX = INPUT('TESTING???') FOR CHECKING TO TEST.
#
#
# Import useful things:
from random import randint
import collections

#Algorithm for each turn.
def PlayTurn():
    Shot1 = 0
    Shot2 = 0
    Score = 0
    Strike = 0      #Set as 0 for normal frame, 1 for spare, 2 for strike.
    
    #Accept input for Frame and validate it.
    Shot1, Shot2 = Validate()

    return (Shot1, Shot2, Shot3)
    
    #Shoot(Shot1, Shot2)

def Shoot(Shot1, Shot2, Shot3, Strikecheck):
    Score = 0
    #TURN THIS INTO A REAL THING!!!
    #Do the shooting stuff.
    if Shot1 == 10:
        Score = 10
        Strike = 2
    elif Shot1 + Shot2 == 10:
        Score = 10
        Strike = 1
    else:
        Score = Shot1 + Shot2
        Strike = 0
        
    Score = Shot1 + Shot2
    pos = 0
    temp = []
    temp.append(Strikecheck)
    for x in Strikecheck:
        
        #Get current value from list
        if x == 2:
            if Shot1 == 10:
                Score += Shot1
                #Tag on new strike check to temp list
                temp.append(x-1)
            elif Shot1 == 10 and Shot2 == 10:
                Score += Shot2
            else:
                Score += Shot1
                Score += Shot2
                temp.append(x-2)
        if x == 1:
            Score += Shot1
            temp.append(x-1)
        if x == 0:
            #Append no strike/spare just to keep the list in place.
            temp.append(x)
    #Shot 3 will always be 0 unless a Spare or 2 strikes have been acheived.
    Score += Shot3
    #Remove now obsolete strike check.       
    del(temp[0])
    del(temp[0])
    #Add newly worked out stike check to end of list.
    temp.append(Strike)
    return (Score, temp)

def Turn10():
    Valid = False
    ShTemp1 = 0
    ShTemp2 = 0
    ShTemp3 = 0
   
    while Valid == False:
        ShTemp1 = int(input('Please enter your first shot: '))
        Valid = ShotValidate(ShTemp1)
        
    Valid = False
    while Valid == False:
        ShTemp2 = int(input('Please enter your second shot: '))
        Valid = ShotValidate(ShTemp2)

    if (ShTemp1 + ShTemp2) >= 10:
        if ShTemp1 == 10 and ShTemp2 != 10:
            ShTemp3 = 0
        else:
            Valid = False
            while Valid == False:
                ShTemp3 = int(input('Please enter third shot: '))
                Valid = ShotValidate(ShTemp3)
    for x in Strikecheck:
        
        #Get current value from list
        if x == 2:
            if Shot1 == 10:
                Score += Shot1
                #Tag on new strike check to temp list
                temp.append(x-1)
            elif Shot1 == 10 and Shot2 == 10:
                Score += Shot2
            else:
                Score += Shot1
                Score += Shot2
                temp.append(x-2)
        if x == 1:
            Score += Shot1
            temp.append(x-1)
        if x == 0:
            #Append no strike/spare just to keep the list in place.
            temp.append(x)
    #Shot 3 will always be 0 unless a Spare or 2 strikes have been acheived.
    Score += Shot3
    #Remove now obsolete strike check.       
    del(temp[0])
    del(temp[0])
    #Add newly worked out stike check to end of list.
    temp.append(Strike)
    return (ShTemp1, ShTemp2, ShTemp3)
    
def Validate():
    Valid = False
    ShTemp1 = 0
    ShTemp2 = 0
    
    while Valid == False:
        ShTemp1 = int(input('Please enter your first shot: '))
        Valid = ShotValidate(ShTemp1)
        
    Valid = False
    
    while Valid == False:
        if ShTemp1 != 10:
            ShTemp2 = int(input('Please enter your second shot: '))
            Valid = ShotValidate(ShTemp2)
            if Valid == True:
                ShTemp1 = int(ShTemp1)
                Valid = TurnValidate(int(ShTemp1),int(ShTemp2))
                if Valid == False:
                    print('Invalid second shot.')
                else:
                    ShTemp2 = int(ShTemp2)
        else:
            Valid = True
    return (ShTemp1, ShTemp2)

def ShotValidate(a):

    Bool = False

    if type(a) == int:
        if a < 0:
            print('Please enter score within valid boundaries of 0-10')
        elif a > 10:
            print('Please enter score within valid boundaries of 0-10')
        else:
            Bool = True
    elif type(a) == str:
        if a < '0':
            print('Please enter value above 0')
        elif a > '10':
            print('Please enter value less than 10')
        else:
            Bool = True
    else:
        print('Incorrect entry... no idea what you did there')
    return Bool

def TurnValidate(a, b):
    Bool = False
    if a+b <= 10:
        Bool = True
    return Bool
    
Striker = [0,0]
Player = ['Luke', 0, Striker]
g = 0

for a in range(1,11):
    if a == 10:
        print(Player[2])
        b, c, d = Turn10()
    e = Player[1]
    b, c, d = PlayTurn()
    e, f = Shoot(b, c, d, Player[2])
    g += e
    del(Player[1])
    del(Player[1])
    Player.append(g)
    Player.append(f)
    
print(Player)

#PlayTurn()

'''
print('Welcome to bowling')
#Set up players
x = 0
Players_key = {}

while x == 0:
    Num = int(input('Enter number of players (max 6) '))
    y = 1
    #Check that appropriate number of players has been entered.
    #TEST: Enter mix of bad numbers and strings.
    if Num > 0 and Num <= 6:
        while Num > 0:
            PName = input('Enter name of player: ')
            Players_key[PName] = []
            Num = Num - 1
            y+=1
        x = 1
    else:
        print('Please enter a sensible number of players')

#Keep entered players in entry order
#Players_actual = collections.OrderdDict(Players_key)

'''
#Display rules and start entering the stuffs.
'''
print("""
Rules for playing:
If you want to manually enter scores, enter: "Play"
If you want to randomise the frame, enter: "Random"
If you want to show the scoreboard, enter: "Score"
If you're bored and want to go home, enter: "Quit"
""")
Playscore = 0
Temp = ''
selection = ''
Quit = False
Turnvalidate = False
#Set loop going for 10 frames.
#3 frame test game
for frame in range(1,3):
    #Set loop going for each players turn within the frame.
    for Temp in Players_key.keys():
            #Finally, implement loop for each shot within players turn.
            if frame == 10:
                #Set 3 shots for final frame.
                x = 3
            else:
                #2 shots otherwise.
                x = 2
            while Turnvalidate == False:
                selection = input('Make selection: ')
                if selection == 'Play' or selection == 'play':
                    FrameScore = PlayTurn()
                    print(FrameScore)
                    #Players_key.keys[Temp].append(FrameScore)
                elif selection == 'Random' or selection == 'random':
                    print(randint(0,10))
                elif selection == 'Quit' or selection == 'quit':
                    Quit = True
                    Turnvalidate = True
                    break
                else:
                    print("""
                    Not a valid choice... friendly reminder:
                    If you want to manually enter scores, enter: "Play"
                    If you want to randomise the frame, enter: "Random"
                    If you want to show the scoreboard, enter: "Score"
                    If you're bored and want to go home, enter: "Quit"
                    """)
            if Quit == True:
                break
            
    if Quit == True:
            break
           
#For shits n giggs.

print(Players_key)
print(Players_actual)
print('Thank you for playing.')
'''
