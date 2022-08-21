x = list(map(int, input().split()))
a, b, c = x[0], x[1], x[2]
count = 0

for i in range(a, b + 1):
    if c % i == 0:
        count += 1

print(count)
