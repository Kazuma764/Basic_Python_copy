class Dice:
    def __init__(self, num):
        self.num_a = num[0]
        self.num_b = num[1]
        self.num_c = num[2]
        self.num_d = num[3]
        self.num_e = num[4]
        self.num_f = num[5]

    def roll_N(self):
        self.num_a, self.num_b, self.num_e, self.num_f = (
            self.num_b,
            self.num_f,
            self.num_a,
            self.num_e,
        )

    def roll_S(self):
        self.num_a, self.num_b, self.num_e, self.num_f = (
            self.num_e,
            self.num_a,
            self.num_f,
            self.num_b,
        )

    def roll_E(self):
        self.num_a, self.num_c, self.num_d, self.num_f = (
            self.num_d,
            self.num_a,
            self.num_f,
            self.num_c,
        )

    def roll_W(self):
        self.num_a, self.num_c, self.num_d, self.num_f = (
            self.num_c,
            self.num_f,
            self.num_a,
            self.num_d,
        )

    def roll(self, dir):
        for i in dir:
            if i == "N":
                dice.roll_N()
            elif i == "S":
                dice.roll_S()
            elif i == "W":
                dice.roll_W()
            else:
                dice.roll_E()

    def return_zero(self):
        return self.num_a


dice_in = list(map(int, input().split()))
roll_direction = input()

dice = Dice(dice_in)

dice.roll(roll_direction)

print(dice.return_zero())


"""
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
"""
