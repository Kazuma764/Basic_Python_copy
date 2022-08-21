X = input()
Y = X.split()
list_i = [int(i) for i in Y]
list_f = [float(j) for j in Y]

a1, b1 = list_i[0], list_i[1]
a2, b2 = list_f[0], list_f[1]

d = a1 // b1
r = a1 % b1
f = a2 / b2

print(d, r, "{:.05f}".format(f))
