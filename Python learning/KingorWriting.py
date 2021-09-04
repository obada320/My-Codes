import random as r

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
            king_or_writing = ['Writing','King']
            total =  r.choice(king_or_writing)
            print(total)
        playagain = input('to roll again press enter and to exit press y : ')


king_or_writing()