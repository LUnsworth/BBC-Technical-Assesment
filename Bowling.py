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

#Define Scoring nonesense
def Score(shot,shnum):
    score = shot
    if shot == 10:
        print('Strike!')
    
    return score

print('Welcome to bowling')
#Set up players
x = 0
Players = {}

while x == 0:
    Num = int(input('Enter number of players (max 6) '))
    y = 1
    #Check that appropriate number of players has been entered.
    #TEST: Enter mix of bad numbers and strings.
    if Num > 0 and Num <= 6:
        while Num > 0:
            PName = input('Enter name of player: ')
            Players[PName] = []
            Num = Num - 1
            y+=1
        x = 1
    else:
        print('Please enter a sensible number of players')
'''
#Display rules and start entering the stuffs.
'''
print("""
Rules for playing:
Enter shot score: 0-10.
If you want to randomise the frame, enter: "Random"
If you want to show the scoreboard, enter: "Score"
If you're bored and want to go home, enter: "Quit"
""")
while 1:
    Playscore = 0
    Temp = ''
    selection = ''
    Quit = False
    #Set loop going for 10 frames.
    for frame in range(1,10):
        print('Frame ',frame,':')
        #Set loop going for each players turn within the frame.
        for Temp in Players.keys():
                #Finally, set loop for each shot within players turn.
                if frame == 10:
                    #Set 3 shots for final frame.
                    x = 3
                else:
                    #2 shots otherwise.
                    x = 2
                    
                for turn in range(1,x):
                    print(Temp,'make your choice for shot ', Temp,':')
                    selection = input('')  

                    if selection >= '0' and selection <= '10':
                        Playscore = Score(int(selection),turn)
                        print(Playscore)                          
                    elif selection[0:] == 'R' or selection[0:] == 'r':
                        print(randint(0,10))
                    elif selection == 'Quit' or selection == 'quit':
                        Quit = True
                        break
                    else:
                        print("""
                        Not a valid choice... friendly reminder:
                        Enter shot score: 0-10.
                        If you want to randomise the frame, enter: "Random"
                        If you want to show the scoreboard, enter: "Score"
                        If you're bored and want to go home, enter: "Quit"
                        """)
        if Quit == True:
             break
    #For shits n giggs.
print(Players)
print('Thank you for playing.')
