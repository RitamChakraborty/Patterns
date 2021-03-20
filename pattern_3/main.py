n = 8

for i in range(n):
    s = ""

    r = range(n - i)

    if i % 2 != 0:
        r = r[::-1]

    for j in r:
        s += str(j + 1)

    print(s)