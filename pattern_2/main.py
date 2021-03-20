n = 5
m = (n * (n + 1)) // 2
k = 0

for i in range(n):
    for j in range(n - i):
        print('\t', (m - k), end="")
        k += 1
    print()
