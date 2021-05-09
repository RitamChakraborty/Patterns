l = range(1, 11)
l1 = []
j = 0

for i in range(1, 5):
    j += i
    k = j - i
    l1.append(l[k:j])

l2 = l1[0:2]
l3 = l1[2:]

a = 0
b = 0

for i in range(4):
    if i % 2 == 0:
        print(l2[a])
        a += 1
    else:
        print(l3[b])
        b += 1
