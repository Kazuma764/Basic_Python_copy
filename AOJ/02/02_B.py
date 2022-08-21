x = input().split()
y = [int(i) for i in x]
a, b, c = y[0], y[1], y[2]

if a < b < c:
    print("Yes")
else:
    print("No")
