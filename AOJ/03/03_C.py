list1 = []

while True:
    x = list(map(int, input().split()))
    if x[0] == 0 and x[1] == 0:
        break
    else:
        list1.append(x)

for i in range(len(list1)):
    list1[i].sort()

for j in range(0, len(list1)):
    print(list1[j][0], list1[j][1])
