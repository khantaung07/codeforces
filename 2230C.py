t = int(input())

for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))

    ones = 0
    big = []

    for x in c:
        if x == 1:
            ones += 1
        elif x >= 2:
            big.append(x)

    if len(big) == 0:
        print(0)

    elif len(big) == 1:
        x = big[0]
        ans = x + min(ones, x // 2)

        if ans < 3:
            print(0)
        else:
            print(ans)

    else:
        ans = sum(big)

        slots = 0
        for x in big:
            slots += x // 2 - 1

        ans += min(ones, slots)

        print(ans)