list_dice = []


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

    def rotate(self):
        self.num_b, self.num_c, self.num_d, self.num_e = (
            self.num_d,
            self.num_b,
            self.num_e,
            self.num_c,
        )

    def mk_same(self):
        for i in range(4):
            for j in range(4):
                self.rotate()
                self.check()
            self.roll_N()

        for i in range(4):
            for j in range(4):
                self.rotate()
                self.check()
            self.roll_E()

    def check(self):
        x = [self.num_a, self.num_b, self.num_c, self.num_d, self.num_e, self.num_f]
        if x in list_dice:
            return
        else:
            list_dice.append(x)

    def compare_dices(self, num, n):
        for i in range(n - 1):
            flag = False
            if num[i + 1] not in list_dice:
                flag = True
            else:
                break
        return flag


dices = []

n = int(input())
for i in range(n):
    x = list(map(int, input().split()))
    dices.append(x)

dice = Dice(dices[0])

dice.mk_same()

if dice.compare_dices(dices, n):
    print("Yes")
else:
    print("No")


"""
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


dices = []

n = int(input())
for i in range(n):
    x = list(map(int, input().split()))
    dices.append(x)

x = dices[0]

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

for i in range(n - 1):
    flag = False
    if dices[i + 1] not in list_dice:
        flag = True
    else:
        break

if flag:
    print("Yes")
else:
    print("No")
"""
