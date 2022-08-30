log = []
log_a1 = []
log_a2 = []
log_a3 = []
log_a4 = []


def print_room(x):
    apart = x
    for i in range(3):
        R = [str(j) for j in apart[i]]
        R = " ".join(R)
        print("", R)


def print_hash():
    print("#" * 20)


def caluculate(x):
    apart = [[0] * 10 for _ in range(3)]
    for i in x:
        if i[1] == 1:
            apart[0][i[2] - 1] += i[3]
        elif i[1] == 2:
            apart[1][i[2] - 1] += i[3]
        else:
            apart[2][i[2] - 1] += i[3]
    return apart


N = int(input())
for i in range(N):
    x = list(map(int, input().split()))
    log.append(x)

for i in log:
    if i[0] == 1:
        log_a1.append(i)
    elif i[0] == 2:
        log_a2.append(i)
    elif i[0] == 3:
        log_a3.append(i)
    else:
        log_a4.append(i)

log_list = [log_a1, log_a2, log_a3, log_a4]

for i in range(len(log_list)):
    apart = caluculate(log_list[i])
    print_room(apart)
    if i == len(log_list) - 1:
        continue
    print_hash()
