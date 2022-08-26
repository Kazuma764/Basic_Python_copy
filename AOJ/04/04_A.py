a, b = map(int, input().split())

d = a // b
r = a % b
f = a / b

print(d, r, "{:.05f}".format(f))
