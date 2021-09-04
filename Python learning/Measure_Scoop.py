from math import pi
from math import pow

print('Welcome in measure scoop')

print('Please choose Type of shape, Enter 1 for Regtangle, Enter 2 for Square, Enter 3 for Circle')

choose = int(input('Enter type:'))

if choose == 1:
    length = float(input('Enter length by meter: '))
    weidth = float(input('Enter weidth by meter: '))
    prem = (length + weidth) * 2
    area = (length * weidth)

    print('This is Premeter' , prem , 'm')
    print('This is Area' , area , 'm2')


elif choose == 2:
    Side = float(input('Enter side length: '))
    prem = Side * 4
    area = Side * Side

    print('This is Premeter' , prem , 'cm')
    print('This is Area' , area , 'cm2')


elif choose == 3:
    d = float(input('Enter diameter: '))
    r = d/2
    prem = (pi * d)
    # area = (pi * r * r)
    area = (pi * pow(r,2))
    
    print('This is Premeter' , prem , 'cm')
    print('This is Area' , area , 'cm2')
else:
    print('You should Enter a valid option, Enter 1 for Regtangle, Enter 2 for Square, Enter 3 for Circle')


input('Press Enter to Exit')