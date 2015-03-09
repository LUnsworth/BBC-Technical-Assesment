#Bowling game source code - BBC Technical exercise - Luke Unsworth 19/02/15
#
# Version 1.0 Completed 09/03/15
# Note: This version works as long as you don't be *too* clever with the inputs.
#       It'll work if you stick to appropriate inputs.
# TODO:
#       Add proper type/input checks and validation. STRING COMPARITORS!!!
#       Add randomise turn functionality.
#       Tidy up code and trim it down where necessary.
#
# Import useful things:
from random import randint
#Global game dictionary. I know this is clunky, but there you go.
Game = {}

def PlayerSetup():
    #Set up players at start of game
    x = 0
    Setup = False
    while Setup == False:
        Num = int(input('Enter number of players (max 6) '))
        y = 1
        #Check that appropriate number of players has been entered.
        #TEST: Enter mix of bad numbers and strings.
        if Num > 0 and Num <= 6:
            for y in range(1,Num+1):
                PName = str(input('Enter name of player: '))
                Game[y] = [PName,0,0,0]
            Setup = True
        else:
            print('Please enter a sensible number of players')

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

#Algorithm for final turn.
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
        Valid = False
        while Valid == False:
            ShTemp3 = int(input('Please enter third shot: '))
            Valid = ShotValidate(ShTemp3)
            if ShTemp1 == 10:
                if ShTemp2 != 10:
                    if ShTemp2 + ShTemp3 > 10:
                        Valid = False
                
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

#Validation for shot input.
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
    #Boolean validation check
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


def Score():
    print('Scores on the doors are...')
    temp = []
    for Player in range(1,len(Game)+1):
        temp = Game[Player]
        print(temp[0], " - ", temp[1])

def Main():
    #Blank list to hold variour player information.
    #Position 0 = Player name
    #Position 1 = Player total score
    #Position 2 = Strike flag from 2 frames prior
    #Position 3 = Strike flag from 1 frame prior
    PlayerList = []
    PlayerScore = 0
    TurnScore = 0
    TurnValidate = False
    Quit = False
    #Populate dict of players. Game{} is global.
    PlayerSetup()
    
    #Display rules and start the game.
    print("""
    Rules for playing:
    If you want to manually enter scores, enter: "Play"
    If you want to randomise the frame, enter: "Random"
    If you want to show the scoreboard, enter: "Score"
    If you're bored and want to go home, enter: "Quit"
    """)
    for Frame in range(1,11):
        #Loop through each key in Game dict.
        for Player in Game:
            #Populate a working list with player entry
            PlayerList = Game[Player]
            PlayerScore = PlayerList[1]
            #Set exit flag again.
            TurnValidate = False
            #Prompt for input.
            while TurnValidate == False:
                print(PlayerList[0], "'s turn.")
                selection = input('Make selection: ')
                if selection == 'Play' or selection == 'play':
                    if Frame == 10:
                        TurnScore = Turn10(PlayerList[2], PlayerList[3])
                    else:
                        TurnScore, PlayerList[2], PlayerList[3]  = PlayTurn(PlayerList[2], PlayerList[3])
                    PlayerScore += TurnScore
                    #Populate new player's Score.
                    PlayerList[1] = PlayerScore
                    TurnValidate = True
                elif selection == 'Random' or selection == 'random':
                    #TODO implement at a later date...
                    print(randint(0,10))
                    print('Feature not available, try another one')
                elif selection == 'Score' or selection == 'score':
                    Score()
                elif selection == 'Quit' or selection == 'quit':
                    Quit = True
                    TurnValidate = True
                    break
                else:
                    print("""
                    Not a valid choice... friendly reminder:
                    If you want to manually enter scores, enter: "Play"
                    If you want to randomise the frame, enter: "Random"
                    If you want to show the scoreboard, enter: "Score"
                    If you're bored and want to go home, enter: "Quit"
                    """)
            Game[Player] = PlayerList
            if Quit == True:
                break        
        if Quit == True:
            break

#Root executer.
print('Welcome to bowling')
Main()
Score()
print('Thank you for playing.')
