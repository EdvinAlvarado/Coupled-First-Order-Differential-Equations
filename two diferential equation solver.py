import numpy as np

M = [[-0.5, 0.5],[0.5,-0.5]]

a = M[0][0]
b = M[0][1]
c = M[1][0]
d = M[1][1]

print('%s \t %s \n %s \t %s \n' %(a,b,c,d))


#test if real or complex
if (a+d)**2 - 4*(a*d - b*c) >= 0:
	r1 = ((a+d) + np.sqrt((a+d)**2 - 4*(a*d - b*c)))/2
	r2 = ((a+d) - np.sqrt((a+d)**2 - 4*(a*d - b*c)))/2
else:
	print('complex number')
print('roots of equation: %s & %s \n' %(r1,r2))

M1 = [[0,0],[0,0]]
M2 = [[0,0],[0,0]]

M1[0][0] = a - r1
M1[1][1] = d - r1
M2[0][0] = a - r2
M2[1][1] = d - r2
M1[0][1] = b
M2[0][1] = b
M1[1][0] = c
M2[1][0] = c
print('root matrices')
print(M1)
print(M2)

ar1 = M1[0][0]
ar2 = M2[0][0]
# print('ar1 %s' %ar1)
# print('ar2 %s' %ar2)

u1 = [-b/ar1, 1]
u2 = [1, -ar2/b]
# print(u1)
# print(u2)

print('x1 = (%s)s1 e^(%st) + (%s)s2 e^(%st)' %(u1[0],r1,u2[0],r2))
print('x2 = (%s)s1 e^(%st) + (%s)s2 e^(%st) \n' %(u1[1],r1,u2[1],r2))