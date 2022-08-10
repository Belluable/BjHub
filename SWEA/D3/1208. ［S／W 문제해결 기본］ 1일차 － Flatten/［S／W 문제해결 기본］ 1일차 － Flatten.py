for tc in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()

    for i in range(n):
        lst[0] += 1
        lst[99] -= 1
        lst.sort()
        if lst[99] - lst[0] <= 1:
            height = lst[99] - lst[0]
            break
    height = lst[99] - lst[0]

    print(f'#{tc} {height}')