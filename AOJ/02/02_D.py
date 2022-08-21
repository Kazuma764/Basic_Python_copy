W, H, x, y, r = map(int, input().split())

a1 = x + r
a2 = x - r
b1 = y + r
b2 = y - r

if a2 >= 0 and a1 <= W and b2 >= 0 and b1 <= H:
    print("Yes")
else:
    print("No")
