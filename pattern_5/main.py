def p(i):
    print("*".join([str(i + 1)] * (i + 1)))


if __name__ == '__main__':
    n = 4
    for i in range(n):
        p(i)

    for i in range(n - 1)[::-1]:
        p(i)
