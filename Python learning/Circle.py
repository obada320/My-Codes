from math import pi
from math import pow


d = int(input('Enter diameter: '))
r = d/2
prem = (pi * d)
# area = (pi * r * r)
area = (pi * pow(r,2))

print('This is Premeter' , prem , 'cm')
print('This is Area' , area , 'cm2')
