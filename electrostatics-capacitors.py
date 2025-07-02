#Task 1
#a
C_1 = 5 * 10**-6
C_2 = 15 * 10 **-6
C_tot = C_1 + C_2
print(C_tot)

#b
U = 100
Q_1 = U * C_1
Q_2 = U * C_2
print(Q_1, Q_2)

#c
R = 1 * 10**6
C = 20 * 10**-6
tk = R * C
print(tk)

#d
print(tk * 5)


#Task 2
#a
#1/C_s = 1/C_1 + 1/C_2 => 1 = C_s * (1/C_1 + 1/C_2) => C_s = 1 / (1/C_1 + 1/C_2)
C_1 = 500 * 10**-9
C_2 = 1.5 * 10**-6
C_3 = 1 * 10**-6
C_s = 1 / (1/C_2 + 1/C_3)
C_t = C_s + C_1
print(C_t)

#b
U = 24
Q_1 = U * C_1
Q_s = U * C_s
print(Q_1, Q_s)

#c
Q_t = Q_s + Q_1
print(Q_t)

#d
U = 24
U_1 = U
U_2 = Q_s / C_2
U_3 = Q_s / C_3
print(U_1, U_2, U_3)

#Task 3
#a
perm_0 = 8.85 * 10**-12
#C = perm_rel * (A/l) => A = (C*l)/perm_rel
C = 5 * 10**-9
perm_rel = perm_0 * 10
l = 0.02 * 10**-3
A = (C*l)/perm_rel
print(A)

#b
U = 100
Q = C * U
print(Q)

#c
C_1 = 5 * 10**-9
C_2 = 0.1 * 10**-6
C_3 = 50 * 10**-9
C_4 = 50 * 10**-9
C_34 = C_3 + C_4
C_23 = 1 / (1/C_2 + 1/C_34)
C_12 = C_23 + C_1
print(C_12)

#d
Q_1 = U * C_1
Q_s = U * C_23
Q_2 = Q_s
Q_34 = Q_s
Q_3 = Q_4 = Q_34/2
print(Q_1, Q_2, Q_3, Q_4)

#e
U = 100
U_1 = Q_1 / C_1
U_s = Q_s / C_23
U_2 = Q_s / C_2
U_34 = Q_s / C_34
U_3 = U_4 = U_34
print(U_1, U_2, U_3, U_4)

#Task 4
#a
C_1 = 15 * 10**-6
C_2 = 8 * 10**-6
C_3 = 10 * 10**-6
C_4 = 5 * 10**-6
C_p = C_2 + C_3
C_t = 1 / (1/C_1 + 1/C_p + 1/C_4)
print(C_t)

#b
U = 60
Q_1 = Q_4 = Q = U * C_t
prop = C_2/(C_3+C_2)
Q_2 = Q*prop
Q_3 = Q - Q_2
print(Q_1, Q_4, Q_2, Q_3)

#c
U_1 = Q_1 / C_1
U_4 = Q_4 / C_4
U_2 = U_3 = U_p = Q / C_p
print(U_1, U_2, U_3, U_4)

#d
U = 60
R_1 = 5 * 10**3
R_2 = 10 * 10**3
R_3 = 15 * 10**3
R_1_prop = R_1/(R_1 + R_2 + R_3)
U_1 = U * R_1_prop
R_2_prop = R_2/(R_1 + R_2 + R_3)
U_2 = U * R_2_prop
R_3_prop = R_3/(R_1 + R_2 + R_3)
U_3 = U * R_3_prop
print(U_1, U_2, U_3)

#e
#Q = C * U
C_1 = 15 * 10**-6
C_2 = 8 * 10**-6
C_3 = 10 * 10**-6
C_4 = 5 * 10**-6
Q_1 = U_1 * C_1
Q_2 = U_2 * C_2
Q_3 = U_2 * C_3
Q_4 = U_3 * C_4
print(Q_1, Q_2, Q_3, Q_4)

#Task 5
#a
U = 24
R_1 = 1 * 10**3
R_2 = 5 * 10**3
C_1 = 500 * 10**-9
C_2 = 1 * 10**-6
C_3 = 4.5 * 10**-6
C_4 = 1 * 10**-6
C_5 = 3 * 10**-6
I = U / (R_1 + R_2)
print(I)

#b
C_124 = C_1 + C_2 + C_4
C_35 = C_3 + C_5
C_t = 1 / (1/C_124 + 1/C_35)
print(C_t)

#c
U_r1 = I * R_1
U_r2 = I * R_2
C_12 = C_1 + C_2
C_12_prop = C_12 / (C_12 + C_3)
U_12 = U * C_12_prop
C_3_prop = C_3 / (C_12 + C_3)
U_3 = U * C_3_prop
C_4_prop = C_4 / (C_4 + C_5)
U_4 = U * C_4_prop
C_5_prop = C_5 / (C_4 + C_5)
U_5 = U * C_5_prop
print(U_r1, U_r2, U_12, U_3, U_4, U_5)

#d
Q_1 = U_12 * C_1
Q_2 = U_12 * C_2
Q_3 = U_3 * C_3
Q_4 = U_4 * C_4
Q_5 = U_5 * C_5
print(Q_1, Q_2, Q_3, Q_4, Q_5)

#Task 6
#a
U = 100
U_r1 = 40
R_2 = 1 * 10**3
R_3 = 5 * 10**3
C_1 = 1 * 10**-6
C_2 = 2 * 10**-6

U_r23 = U - U_r1
R_2_prop = R_2 / (R_2 + R_3)
U_r2 = U_r23 * R_2_prop
I = U_r2 / R_2
print(I)

#b
R_1 = U_r1 / I
print(R_1)

#c
U_r3 = U - U_r1 - U_r2
print(U_r1, U_r2, U_r3)

#d
U_c2 = U_r3
U_c1 = U - U_r1
Q_1 = U_c1 * C_1
Q_2 = U_c2 * C_2
print(Q_1, Q_2)