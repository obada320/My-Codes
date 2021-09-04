import random as r

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


Guess()