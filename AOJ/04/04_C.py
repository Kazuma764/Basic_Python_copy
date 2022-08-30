list1 = []

while True:
    Y = input().split()
    a, b = int(Y[0]), int(Y[2])
    if Y[1] == "+":
        list1.append(a + b)
    elif Y[1] == "-":
        list1.append(a - b)
    elif Y[1] == "*":
        list1.append(a * b)
    elif Y[1] == "/":
        list1.append(a // b)
    if Y[1] == "?":
        break

[print(i) for i in list1]
