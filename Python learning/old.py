name1 = str(input('Enter name '))
age1 = float(input('Enter age  '))

name2 = str(input('Enter name '))
age2 = float(input('Enter age '))

name3 = str(input('Enter name '))
age3 = float(input('Enter age '))

if age1 > age2:
    if age1 > age3:
        print(name1,' is the oldest')

if age2 > age1:
    if age2 > age3:
        print(name2, ' is the oldest')
    
if age3 > age1:
    if age3 > age2:
        print(name3, ' is the oldest')