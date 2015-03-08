#Bowling game source code - BBC Technical exercise - Luke Unsworth 19/02/15
#
# TODO:
#   - Write scoring "engine"
#      - Function?
#   - Create class of "Frame".
#      - Int Shot1
#      - Int Shot2
#      - Int Total (because of strikes and stuff)
#   - Create class of "Player"
#      - Array of 10 "Frame".
#      - String "PlayerName"
#      - Int "PlayerScore"
#
#   Create Dict of players.
#   
#   - Testing:
#      - MAKE SURE TO USE THE "XXX = INPUT('TESTING???') FOR CHECKING TO TEST.
#
#
# Import useful things:
from random import randint
import collections

#Algorithm for each turn.
def PlayTurn(Strike1, Strike2):
    Shot1 = 0
    Shot2 = 0
    Score = 0
    
    #Accept input for Frame and validate it.
    Shot1, Shot2 = Validate()
    #Calculate any additional Strike/Spare bonuses and return new strike flags.
    Score, Strike1, Strike2 = Shoot(Shot1, Shot2, Strike1, Strike2)

    return (Score, Strike1, Strike2)
    

def Shoot(Shot1, Shot2, Strike1, Strike2):
    Score = 0
    #Do the shooting stuff.
        
    Score = Shot1 + Shot2
    Strikecheck = [Strike1, Strike2]
    for x in range(0,2):
            #Get current value from list
            if Strikecheck[x] == 2:
                if Shot1 == 10:
                    Score += Shot1
                    #Tag on new strike check to temp list
                    Strikecheck[x] = 1
                else:
                    Score += Shot1
                    Score += Shot2
                    Strikecheck[x] = 0
            elif Strikecheck[x] == 1:
                Score += Shot1
                Strikecheck[x] = 0
    
    Strikecheck[0] = Strikecheck[1]
    
    if Shot1 == 10:
            Strikecheck[1] = 2
    elif Shot1 + Shot2 == 10:
            Strikecheck[1] = 1
    else:
            Strikecheck[1] = 0
    
    return (Score, Strikecheck[0], Strikecheck[1])

def Turn10(Strike1, Strike2):
    Valid = False
    ShTemp1 = 0
    ShTemp2 = 0
    ShTemp3 = 0
    Score = 0
   
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
                
    temp = [Strike1, Strike2]
    #Tot up all the shots. If the third shot isn't attained
    #ShTemp3 = 0 so we're fine to do this
    Score = ShTemp1 + ShTemp2 + ShTemp3
    for x in temp:  
        #Get current value from list
        if x == 2:
            Score += ShTemp1
            Score += ShTemp2
        if x == 1:
            Score += ShTemp1
    #Remove now obsolete strike check.     
    return Score
    
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


TurnScore = 0
PlayerScore = 0
Player = ['Luke', 0, 0, 0]

for a in range(1,11):
    PlyaerScore = Player[1]
    if a == 10:
        TurnScore = Turn10(Player[2], Player[3])
    else:
        TurnScore, Player[2], Player[3]  = PlayTurn(Player[2], Player[3])
    PlayerScore += TurnScore
    #Populate new player's Score.
    Player[1] = PlayerScore
    
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
