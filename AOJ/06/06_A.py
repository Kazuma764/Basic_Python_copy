n = int(input())
x = list(map(int, input().split()))

if n % 2 == 0:
    m = int(n / 2)
else:
    m = n // 2

for i in range(m):
    a = x[i]
    x[i] = x[-i - 1]
    x[-i - 1] = a

L = " ".join(map(str, x))
print(L)
