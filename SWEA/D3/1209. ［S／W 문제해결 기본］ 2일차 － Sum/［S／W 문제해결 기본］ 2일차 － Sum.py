
while True:
    try:
        tc = int(input())
        lst = [list(map(int, input().split())) for _ in range(100)]
        ans = 0
        for i in range(100):
            s = 0
            for j in range(100):
                s += lst[i][j]
            if ans < s:
                ans = s

        for j in range(100):
            s = 0
            for i in range(100):
                s += lst[i][j]
            if ans < s:
                ans = s

        s = 0
        for i in range(100):
            s += lst[i][i]
            if ans < s:
                ans = s

        s = 0
        for i in range(100):
            s += lst[i][99-i]
            if ans < s:
                ans = s

        print(f'#{tc} {ans}')

    except:
        break