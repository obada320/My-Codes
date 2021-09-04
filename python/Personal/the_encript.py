def PRINT(*wwrd):
    print(*wwrd)



A = '010'
B = '011001'
C = '011000'
D = '01111'
E = '01110'
F = '01101'
G = '01100'
H = '0111'
I = '0110'
J = '011'
K = '011010'
L = '011011'
M = '011100'
N = '011101'
O = '011110'
P = '011111'
Q = '0110000'
R = '0110001'
S = '0110010'
T = '0110011'
U = '0110101'
V = '0110110'
W = '0110111'
X = '0111000'
Y = '011100100'
Z = '0111001001'
w1 = A
w2 = S
w3 = D
w4 = F
w5 = G
w6 = H
w7 = J
w8 = K
w9 = L
w0 = M
A2 = bin(0).replace('b','')
B2 = bin(9).replace('b','')
C2 = bin(8).replace('b','')
D2 = bin(7).replace('b','')
E2 = bin(6).replace('b','')
F2 = bin(5).replace('b','')
G2 = bin(4).replace('b','')
H2 = bin(3).replace('b','')
I2 = bin(2).replace('b','')
J2 = bin(1).replace('b','')
K2 = bin(10).replace('b','')
L2 = bin(11).replace('b','') 
M2 = bin(12).replace('b','')
N2 = bin(13).replace('b','')
O2 = bin(14).replace('b','')
P2 = bin(15).replace('b','')
Q2 = bin(16).replace('b','')
R2 = bin(17).replace('b','')
S2 = bin(18).replace('b','')
T2 = bin(19).replace('b','')
U2 = bin(20).replace('b','')
V2 = bin(21).replace('b','')
W2 = bin(22).replace('b','')
X2 = bin(23).replace('b','')
Y2 = bin(24).replace('b','')                                                                    
Z2 = bin(100).replace('b','')
w1 = A2
w2 = S2
w3 = D2
w4 = F2
w5 = G2
w6 = H2
w7 = J2
w8 = K2
w9 = L2
w0 = M2

while True:
    num = input()
    if num == '':
        PRINT('INVALID')
    else:
        num = int(num)
        print(bin(num).replace('b',''))