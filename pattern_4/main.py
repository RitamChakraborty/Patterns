n = 11
l = []

for i in range(n):
    l1 = []
    for j in range(i + 1):
        if 0 < j < i:
            l1.append(l[j - 1] + l[j])
        else:
            l1.append(1)

    l.clear()
    l.extend(l1)
    print("\t" * (n - i), end="")
    print("\t\t".join(list(map(str, l))))
