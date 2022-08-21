x = input().split()
y = [int(i) for i in x]
a, b = y[0], y[1]

if a < b:
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("a == b")
