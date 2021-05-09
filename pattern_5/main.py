def p(i):
    print("*".join([str(i + 1)] * (i + 1)))

for i in range(4):
    p(i)

for i in range(3)[::-1]:
    p(i)
