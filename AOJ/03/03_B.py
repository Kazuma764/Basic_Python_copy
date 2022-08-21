list = []
flag = True

while flag:
    x = int(input())
    if x == 0:
        break
    else:
        list.append(x)

for i in range(len(list)):
    print("Case ", i + 1, ": ", list[i], sep="")
