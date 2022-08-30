mark_list = ["S", "H", "D", "C"]
num_list = list(range(1, 14))
num_list = [str(i) for i in num_list]
S_list = []
H_list = []
C_list = []
D_list = []
card_list = []
answer = []


def remove_list(x):
    length = len(x)
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    for i in range(length):
        if x[i][1] in numbers:
            numbers.remove(x[i][1])
    return numbers


N = int(input())

for i in range(N):
    card = input().split()
    card_list.append(card)

for i in card_list:
    if i[0] == "S":
        S_list.append(i)
    elif i[0] == "H":
        H_list.append(i)
    elif i[0] == "C":
        C_list.append(i)
    else:
        D_list.append(i)

S_num = remove_list(S_list)
H_num = remove_list(H_list)
C_num = remove_list(C_list)
D_num = remove_list(D_list)

for i in range(len(S_num)):
    print("S", S_num[i])
for j in range(len(H_num)):
    print("H", H_num[j])
for k in range(len(C_num)):
    print("C", C_num[k])
for n in range(len(D_num)):
    print("D", D_num[n])
