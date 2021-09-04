people,ic3craem = map(int,input().split())
Sad = 0

i = 0
while i != people:
    mark , ic3cam = input().split()
    ic3cam = int(ic3cam)

    if mark == '+':
        ic3craem += ic3cam
    elif mark == '-':
        if ic3cam > ic3craem:
            Sad += 1
        else:
            ic3craem -= ic3cam
    else:
        print('invalid') 
           
    i += 1
print(ic3craem,Sad)