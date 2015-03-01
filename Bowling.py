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
    Valid = False
    ShTemp1 = 0
    ShTemp2 = 0
    Score = 0
    while Valid == False:
        ShTemp1 = input('Please enter your first shot: ')
        Valid = TurnValidate(ShTemp1, ShTemp2)
        if Valid == True:
            ShTemp2 = input('Please enter your second shot: ')
            Valid = TurnValidate(ShTemp1, ShTemp2)
            if Valid == True:
                Score = int(ShTemp1) + int(ShTemp2)
    return Score    

def TurnValidate(a, b):
    Bool = False
    #Perform check on shot types, ranges and total value of each.
    if type(a) == 'int':
        if a < 0 or a > 10:
            print('Please enter score within valid boundaries of 0-10')
    elif type(b) == 'int':
        if a < 0 or a > 10:
            print('Please enter score within valid boundaries of 0-10')
    else:
        if a < '0' or a > '10':
            print('Please enter score within valid boundaries of 0-10')
        else:
            a = int(a)
        elif (int(a) + int(b)) > 10: 
            print("That's not a valid combination now, is it?")
        else:
            Bool = True
    elif: type(a) == 'int':
        if a < 0 or a > 10:
            print('Please enter score within valid boundaries of 0-10')
        elif (int(a) + int(b)) > 10:
            print("That's not a valid combination now, is it?")
        else:
            Bool = True
    return Bool

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
