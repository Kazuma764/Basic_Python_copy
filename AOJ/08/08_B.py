flag = True
list_in = []
list_number = []
count = 0


def devider(k):
    list_in = []
    while k > 0:
        list_in.append(k % 10)
        k //= 10
    list_in.reverse()
    return list_in


while flag is True:
    x = int(input())
    if x == 0:
        break
    else:
        list_number.append(devider(x))


while flag is True:
    if count == len(list_number):
        break
    else:
        print(sum(list_number[count]))
        count += 1
