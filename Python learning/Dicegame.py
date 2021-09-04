from random import randint

def Dice():
    play = input('Press Enter to roll and press y to Exit : ')

    if play == 'y':
        exit()
    else:
        print(randint(1,6))

    playagain = input('to roll again press enter and to exit press y : ')

    while playagain != 'y':
        if playagain == 'y':
            exit()
        else:
            print(randint(1,6))
        playagain = input('to roll again press enter and to exit press y : ')

Dice()