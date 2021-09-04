print('Wellcome to culclator')

while True:
    num1 , mark , num2 = input().split()
    mum1 = int(num1)
    mum2 = int(num2)
    marc = str(mark)

    if marc == '+':
        print(mum1 + mum2)
    elif marc == '*':
        print(mum1 * mum2)
    elif marc == '÷' or marc == '/':
        print(mum1 / mum2)
    elif marc == '-':
        print(mum1 - mum2)
