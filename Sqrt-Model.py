from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

mstrlist = []
planelist = []
dlist = []

def f(a, b, c, d):
	return (a+d)**2 - 4 * (a*d - b*c)
def fB(a, B, d):
	return (a+d)**2 - 4 * (a*d - B)


test_range = range(-20, 20)

# for a in test_range:
# 	for d in test_range:
# 		for b in test_range:
# 			for c in test_range:
# 				# mstrlist.append([a, b, c, d, f(a, b, c, d), a*d, b*c,  (f(a, b, c, d) < 0), (a*d < True), (b*c < True)])
# 				# mstrlist.append([a*d, B, f(a, B, d)])
# 				mstrlist.append([a*d, b*c, f(a, b, c, d)])

for a in test_range:
	for d in test_range:
		for B in range(-200, 200):
			dlist.append(d)
			mstrlist.append([a*d, B, fB(a, B, d)])
			# planelist.append(0)


# print(mstrlist)

# for lst in mstrlist:
# 	if lst[4] is True:
# 		print(lst)

# f = open("data.txt", "w")
# for lst in mstrlist:
# 	for item in lst:
# 		f.write("%i\t" % item)
# 	f.write("\n")

# f.close()


A = [lst[0] for lst in mstrlist]
B = [lst[1] for lst in mstrlist]
F = [lst[2] for lst in mstrlist]
# x = np.linspace(-10, 10)
# y = np.linspace(-10, 10)
# X, Y = np.meshgrid(x, y)
# def Zero(x, y):
# 	return 0*x + 0*y
# Z = Zero(X, Y)


fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
ax = plt.axes(projection='3d')
ax.scatter3D(A, B, F, c=F, cmap='Greens')
# ax.scatter3D(A, B, planelist, c=F, cmap='Reds')
# ax.scatter3D(A, B, F, c=F, cmap='Greens')
# ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('A')
ax.set_ylabel('B')
ax.set_zlabel('F')
plt.show()
