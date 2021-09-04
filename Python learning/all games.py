# library import
import random as r
# Games
def king_or_writing():
    play = input('press enter to roll and press y to close\exit ')

    if play == 'y':
        exit()
    else:
        king_or_writing = ['King','Writing']
        total =  r.choice(king_or_writing)
        print(total)

    playagain = input('to roll again press enter and to exit press y : ')

    while playagain != 'y':
        if playagain == 'y':
            exit()
        else:
            king_or_writing = ['King','Writing']
            total =  r.choice(king_or_writing)
            print(total)
        playagain = input('to roll again press enter and to exit press y : ')

def Guess():
    in1 = int(input('Guess a number between 0 and 100 : '))
    num = r.randint(0,100)
    while in1 != num:
        if in1 < num:
            print('Enter Greater number')
        elif in1 > num:
            print('Enter A smaller Number')
        in1 = int(input('Guess a number between 0 and 100 : '))
    print('Cronglations 🎈 You Won')
    input('Press Enter to Exit')

def Dice():
    play = input('Press Enter to roll and press y to Exit : ')

    if play == 'y':
        exit()
    else:
        print(r.randint(1,6))

    playagain = input('to roll again press enter and to exit press y : ')

    while playagain != 'y':
        if playagain == 'y':
            exit()
        else:
            print(r.randint(1,6))
        playagain = input('to roll again press enter and to exit press y : ')

# Game
print('for king or writing type 1, for Guess Game type 2 and for Dice Game type 3 ')
choose = input('Choose : ')

if choose == '1':
    king_or_writing()
elif choose == '2':
    Guess()
elif choose == '3':
    Dice()
else:
    print('invalid')