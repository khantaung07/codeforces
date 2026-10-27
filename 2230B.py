t = int(input())

for _ in range(t):
    s = input().strip()

    # consider all multiples of 4 less than 4 digits

    # 4 (remove all 4s)
    # 12
    # 24 (remove all 4s)
    # 32
    # 44 (remove all 4s)
    # and then all of these with 1, 2, 3, 4 before them


    # remove all 4s
    removed_4 = s.count('4')
    s = s.replace('4', '')

    # now we need the remaining string to have all 2s before all 1s/3s.
    # try every split:
    # delete 1/3s on the left + delete 2s on the right.
    total_2 = s.count('2')
    left_13 = 0
    right_2 = total_2

    best = right_2  # split before the whole string

    for ch in s:
        if ch == '2':
            right_2 -= 1
        else:  # ch is '1' or '3'
            left_13 += 1

        best = min(best, left_13 + right_2)

    print(removed_4 + best)