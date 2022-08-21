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


dice_in = list(map(int, input().split()))
roll_direction = input()

for i in roll_direction:
    if i == "N":
        dice_in = roll_N(dice_in)
    elif i == "S":
        dice_in = roll_S(dice_in)
    elif i == "W":
        dice_in = roll_W(dice_in)
    else:
        dice_in = roll_E(dice_in)

print(dice_in[0])
