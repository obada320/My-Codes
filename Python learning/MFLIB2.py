import math
from the_encript import O, X
#This is My function Library
def simple1(Start,End,Step,str1):
    for i in range(Start,End + 1,Step):
        print(f'{str1} {i}')

def simple2(Start,End,Step):
    for i in range(Start,End,Step):
        print(i)

def simple3(int1,int3):
    i = 0
    while int1 >= int3:
        print(i)
    i += 1

def simple4(int1,int2,str1):
    i = 0
    while int1 <= int2:
        print(str1)
    i += 1

def write1(*str1):
    for i in str1:
        print(str1)

def write2(str1 = 'None'):
    print(str1)

def write3(str1 = 'None',str2 = 'None'):
    print(str1,str2,)

def write4(str1 = 'None',str2 = 'None',str3 = 'None'):
    print(str1,str2,str3)

def write5(str1 = 'None',str2 = 'None',str3 = 'None'):
    print(str1,str2,str3)

def Write(*str1):
    print(*str1)

def Character(name = 'Not imported',nickname = 'Not imported',age = 'Not imported',country = 'Not imported'):
    print('Hello',name,'your Age is :')
    print(age)
    print('And your Nickname is :')
    print(nickname)
    print('And your Country is:')
    print(country)

def user(User = 'Unown',Nickname = 'No Nickname',first = 'Unown',middel = 'Unown',end = 'Unown',age = 'Unown',mail = 'No Mail',password = 'No Password',Country = 'No Country',Region = 'No imported',Family_Name = 'No Family',family_surname = 'No Family surname'):
    print('Hello',User)
    print('your Nickname is:',Nickname)
    print('your first name is:',first)
    print('your middel name is:',middel)
    print('your last name is:',end)
    print('you are is:',age)
    print('your mail is:',mail)
    print('re enter your Password to contnue' )
    password2 = input('Re Enter your password')
    if password2 == password:
        print(password)
    else:
        exit()
    print(Country)
    print(Region)
    print(Family_Name)
    print(family_surname)

def Min(list):
    List = list[0]
    for i in list:
        if i < List:
            List = i
    return List

def Max(list1):
    List1 = list1[0]
    for i in list1:
        if i > List1:
            List1 = i
    return List1

def data(*in1):
    data1 = in1
    return in1

def close():
    exit()

def LS(list,key):
    for i in list:
        if i == key:
            return 'Found'
    return 'Not Found'

def in1(message):
    input(message,)

def CMA(YEAROFBIRTH,NAME = 'Unown'):
    age = 2021 - YEAROFBIRTH
    return f'Your age is {age} {NAME}'

def CMY(AGE,NAME = 'Unown'):
    yearofbirth = 2021 - AGE
    return f'Your year of birth is {yearofbirth} {NAME}'

def printer(Toprint,much : int = 1):
    TP = Toprint
    for i in range(much):
        print(TP)

def IDmak(age, level = '9'):
    if level == 'L' or 1 or '1':
        ID1 = age + 3332323 * 8323245545642332 // 4 + 'wda' + 76454565443665643 + 'jds' + 566546657
        return ID1
    elif level == 'M' or 2 or '2':
        ID2 = age + 6233243434 * 103424564534223 // 3 + 94898547894769876 + 'jihjdiufhsd45545iufhdsiuf546546456hpodjsdio3435423uhf'
        return ID2
    else:
        ID3  = age + 10972232332435469 * 114354332232323 // 2 + 'j45n5i64hjoiu23094ru43ud9w8rh3948dnm4398run398uf4589tu459fun'
        return ID3

def BS(list):
    LEN = len(list)
    for j in range(LEN):
        for i in range(LEN-1-j):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
    return list

def INS(list):
    L = len(list)
    for i in range(1,L):
        key = list[i]
        j = i - 1
        while j >= 0:
            if key < list[j]:
                list[j+1] = list[j]
                list[j] = key
            j = j - 1
    return list

def MMX(list):
    big = Max(list)
    small = Min(list)
    return big - small

def add(word):
    print("word without dot's : ",word)
    total = '.'.join(word[i] for i in range(len(word)))
    return total

def add2(word):
    t = word.replace("",".")
    return t

