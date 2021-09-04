import MFLib as f
#the variables
CMAORCMY = input('if you want to calculate your age type CMA if you want to calculate your year of birth type CMY : ')
if CMAORCMY == 'CMA':
    YB = int(input('Enter year of birth : '))
    NAM = input('Enter your name : ')
    if NAM == '':
        print('Please Enter your Name')
        NAM = input('Re-Enter your name : ')
    CMA = f.CMA(YB,NAM)
    print(CMA)
elif CMAORCMY == 'CMY':
    AG = int(input('Enter your Age : '))
    NAM3 = input('Enter your name : ')
    if NAM3 == '':
        print('Please Enter your Name')
        NAM3 = input('Re-Enter your name : ')
    CMY = f.CMY(AG,NAM3)
    print(CMY)

input('Press Enter to Exit')