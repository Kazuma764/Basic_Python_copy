list_dice = []


def roll_N(x):
    dice = [0] * 6
    dice[0] = x[1]
    dice[1] = x[5]
    dice[2] = x[2]
    dice[3] = x[3]
    dice[4] = x[0]
    dice[5] = x[4]
    return dice


def roll_S(x):
    dice = [0] * 6
    dice[0] = x[4]
    dice[1] = x[0]
    dice[2] = x[2]
    dice[3] = x[3]
    dice[4] = x[5]
    dice[5] = x[1]
    return dice


def roll_E(x):
    dice = [0] * 6
    dice[0] = x[3]
    dice[1] = x[1]
    dice[2] = x[0]
    dice[3] = x[5]
    dice[4] = x[4]
    dice[5] = x[2]
    return dice


def roll_W(x):
    dice = [0] * 6
    dice[0] = x[2]
    dice[1] = x[1]
    dice[2] = x[5]
    dice[3] = x[0]
    dice[4] = x[4]
    dice[5] = x[3]
    return dice


def rotate(x):
    dice = [0] * 6
    dice[0] = x[0]
    dice[1] = x[3]
    dice[2] = x[1]
    dice[3] = x[4]
    dice[4] = x[2]
    dice[5] = x[5]
    return dice


def check(x):
    if x in list_dice:
        return
    else:
        list_dice.append(x)


x = list(map(int, input().split()))
y = list(map(int, input().split()))

for i in range(4):
    for j in range(4):
        x = rotate(x)
        check(x)
    x = roll_N(x)

for i in range(4):
    for j in range(4):
        x = rotate(x)
        check(x)
    x = roll_E(x)

if y in list_dice:
    print("Yes")
else:
    print("No")
