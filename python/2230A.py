t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    groups = n // 3
    rem = n % 3

    ans = groups * min(3 * a, b)

    if rem == 1:
        ans += min(a, b)
    elif rem == 2:
        ans += min(2 * a, b)

    print(ans)