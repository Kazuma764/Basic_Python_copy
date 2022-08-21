same = [
    [0, 1, 2, 3, 4, 5],
    [0, 2, 4, 1, 3, 5],
    [0, 4, 3, 2, 1, 5],
    [0, 3, 1, 4, 2, 5],
    [1, 5, 2, 3, 0, 4],
    [1, 2, 0, 5, 3, 4],
    [1, 0, 3, 2, 5, 4],
    [1, 3, 5, 0, 2, 4],
    [2, 1, 5, 0, 4, 3],
    [2, 5, 4, 1, 0, 3],
    [2, 4, 0, 5, 1, 3],
    [2, 0, 1, 4, 5, 3],
    [3, 0, 4, 1, 5, 2],
    [3, 4, 5, 0, 1, 2],
    [3, 5, 1, 4, 0, 2],
    [3, 1, 0, 5, 4, 2],
    [4, 0, 2, 3, 5, 1],
    [4, 2, 5, 0, 3, 1],
    [4, 5, 3, 2, 0, 1],
    [4, 3, 0, 5, 2, 1],
    [5, 4, 2, 3, 1, 0],
    [5, 2, 1, 4, 3, 0],
    [5, 1, 3, 2, 4, 0],
    [5, 3, 4, 1, 2, 0],
]

length = len(same)


def change(x, y):
    dice = [0] * 6
    dice[0] = x[y[0]]
    dice[1] = x[y[1]]
    dice[2] = x[y[2]]
    dice[3] = x[y[3]]
    dice[4] = x[y[4]]
    dice[5] = x[y[5]]
    return dice


dices = []
n = int(input())
for i in range(n):
    x = list(map(int, input().split()))
    dices.append(x)

for i in range(n - 1):
    flag = False
    for j in range(length):
        check = change(dices[i + 1], same[j])
        if check == dices[0]:
            flag = True
    if flag:
        break

if flag:
    print("No")
else:
    print("Yes")
