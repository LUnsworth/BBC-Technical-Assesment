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
#   - Testing:
#       - MAKE SURE TO USE THE "XXX = INPUT('TESTING???') FOR CHECKING TO TEST.
#
#   - Create and populate list of players
#   - THEN come up with way of 
#
#
# Import useful things:
from random import randint
'''
class Frame:      

class Player:
    def PlayerName:
        print(PlayerName)
'''
print('Welcome to bowling')
#Set up players
x = 0
Players = []
while x == 0:
    Num = int(input('Enter number of players (max 6) '))
    y = 1
    #Check that appropriate number of players has been entered.
    #TEST: Enter mix of bad numbers and strings.
    if Num > 0 and Num <= 6:
        while Num > 0:
            Name = input('Enter name of player: ')
            Players.append(Name)
            Num = Num - 1
            y+=1
        x = 1
    else:
        print('Please enter a sensible number of players')
#Display rules and start entering the stuffs.
print("""
Rules for playing:
Enter first shot score: 0-10.
If you want to randomise the frame, enter: "Random"
If you want to show the scoreboard, enter: "Score"
If you're bored and want to go home, enter: "Quit"
""")
while 1:
#
    Temp = ''
    Quit = False
    for Temp in Players.items():
            print(Temp,'make your choice:')
            selection = input('')  
            if selection >= "0" and selection <= "10":
                print(selection)
            elif selection[0] == 'Random' or selection[0] == 'random':
                print(randint(0,10))
            elif selection == 'Quit' or selection == 'quit':
                Quit = True
                break
            else:
                print("""
                Rules for playing:
                Enter first shot score: 0-10.
                If you want to randomise the frame, enter: "Random"
                If you want to show the scoreboard, enter: "Score"
                If you're bored and want to go home, enter: "Quit"
                """)
    if Quit == True:
            break
    #For shits n giggs.
print(Players)
print('Thank you for playing.')
