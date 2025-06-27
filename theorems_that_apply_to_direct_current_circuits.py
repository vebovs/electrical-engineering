#Task 1
#a
E_el = 1.5
n = 4
E_t = 1.5*4
print(E_t)

#b
R_el = 0.3
n = 4
R_b = R_el*n
print(R_b)

#c
I = 20 * 10**-3
E = 1.5
R_i = 0.3
U_i = I * R_i
U_y = E - U_i
print(U_y*n)

#d
R_y = U_y/I
print(R_y*n)

#e
E = 1.5
R_i = 0.3
I = E/R_i
print(I)

#Task 2
#a
"""
ems blir da E = 12
"""

#b
R_i = 0.03
n = 3
R_b = R_i/n
print(R_b)

#c
I = 300
U_i = I * R_b
E = 12
U_y = E - U_i
print(U_y)

#d
E = 12
I = E/R_i
n = 3
print(I*3)

#Task 3
#a
E_n = 2
n = 6
ems = E_n * n
print(ems)

#b
R_i = 0.005
n = 6
R_it = R_i * n
print(R_it)

#c
n = 6
E_n = 2
E_t = E_n * n
I = 200
U_it = E_t - I * R_it
U_yt = E_t - U_it
print(U_yt)

#d
R_yt = U_yt/I
print(R_yt)

#e
n = 6
E_n = 2
E_t = E_n * n
R_i = 0.005
R_it = R_i * n
I = E_t/R_it
print(I)

#Task 4
#a
"""
U_y = E
"""

#b
R_i = 0.3
E = 24
I = 5
U_i = I * R_i
U_y = E - U_i
print(U_y)

#c
R_L = U_y/I
print(R_L)

#d
"""
0V, siden det ikke er noe som belaster kretsen
"""

#e
E = 24
R_i = 0.3
I = E/R_i
print(I)

#Task 5
#a
R_1 = 25
R_2 = 15
R_i = 0.4
R_l1 = R_l2 = 0.2
R_t = R_1 + R_2 + R_i + R_l1 + R_l2
print(R_t)

#b
E = 12
I = E/R_t
print(I)

#c
U_i = R_i * I
print(U_i)

#d
U_y = E - U_i
print(U_y)

#e
"""
Samme som U_i
"""

#f
U_1 = R_1 * I
U_2 = R_2 * I
print(U_1, U_2)

#Task 6
#a
U = 10
R_1 = R_2 = 10 * 10**3
R_th = R_1/2
print(R_th)
prop = R_1/(R_1 + R_2)
U_th = U * prop
print(U_th)

#b
R_1 = R_2 = 10 * 10**3
R_n = R_1/2
print(R_n)
I_n = U_th/R_n
print(I_n)
