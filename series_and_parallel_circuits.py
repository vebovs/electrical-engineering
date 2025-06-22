#Task 1
#a
"""
U = U_1 + U_2 + U_3 + ...
"""

#b
U_r1 = 15
U_r2 = 5
U_r3 = 30
U_t = U_r1 + U_r2 + U_r3
print(U_t) #50V

#c
"""
Samme, 10mA
"""

#d
I = 10 * 10**-3
U_r1 = 15
U_r2 = 5
U_r3 = 30
R_1 = U_r1/I
R_2 = U_r2/I
R_3 = U_r3/I
print(R_1, R_2, R_3)

#Task 2
#a
"""
Samme, 0.5A
"""

#b
U = 200
I = 0.5
R = U/I
print(R)

#c
R_tot = 400
R_1 = 200
R_2 = 100
R_3 = 50
R_4 = R_tot - R_1 - R_2 - R_3
print(R_4)

#d
R_1 = 200
R_2 = 100
R_3 = 50
R_4 = 50
I = 0.5
U_1 = I*R_1
U_2 = I*R_2
U_3 = I*R_3
U_4 = I*R_4
print(U_1, U_2, U_3, U_4)

#Task 3
#a
R_1 = 200
R_2 = 400
R_t = R_1 + R_2
print(R_t)

#b
R = 600
U = 48
I = U/R
print(I) 

#c
R_1 = 200
I = 0.08
U_1 = I*R_1
print(U_1)

#d
R_2 = 400
I = 0.08
U_2 = I*R_2
print(U_2)

#Task 4
I = 50 * 10**-6
R_i = 1000
U_1 = 1
R_1 = (U_1/I) - R_i
U_2 = 5
R_2 = (U_2/I) - R_i - R_1
U_3 = 25
R_3 = (U_3/I) - R_i - R_1
U_4 = 50
R_4 = (U_4/I) - R_i - R_1
U_5 = 250
R_5 = (U_5/I) - R_i - R_1
print(R_1, R_2, R_3, R_4, R_5)

#Task 5
#a
I = 2
U = 20
R = U/I
print(R)

#b
R = 100
I = 2
U = R*I
print(U)

#c
U = 440
U_1 = 20
U_2 = 200
U_3 = U - U_1 - U_2
print(U_3)

#d
U_3 = 220
I = 2
R_3 = U_3/I
print(R_3)

#Task 6
#a
"""
I = I_1 + I_2 + ...
"""

#b
R_1 = 4
R_2 = 6
#1/R_t = 1/R_1 + 1/R_2 => 1/4 + 1/6 = 3/12 + 2/12 = 5/12 => 5/12 * R_t = 1 => R_t = 1/(5/12) = 12/5
R_t = 12/5
print(R_t)

#c
R = 2.4
U = 24
I = U/R
print(I)

#d
R_1 = 4
R_2 = 6
U = 24
I_1 = U/R_1
I_2 = U/R_2
print(I_1, I_2)

#Task 7
#b
U = 240
I = 12
R = U/I
print(R)

#c
R_t = 20
#R_i/n = R_t
R_i = R_t * 3
print(R_i)

#Task 8
#a
R_t = 100/3
print(R_t)

#b
U = 220
R = 100/3
I = U/R
print(I)

#c
U = 220
R_1 = 100
I_1 = U/R_1
print(I_1)

#d
U = 220
R_2 = 50
I_2 = U/R_2
print(I_2)
