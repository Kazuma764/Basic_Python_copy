n = int(input())
x = list(map(int, input().split()))

if n % 2 == 0:
    m = int(n / 2)
else:
    m = n // 2

x = x[::-1]

L = " ".join(map(str, x))
print(L)
