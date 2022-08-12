t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    lst = [0]*200   # 통로
    mx = 0
    for now, home in arr:
        # 뒷방에서 앞방인 경우
        if now > home:
            now, home = home, now
        
        # 홀짝 한번에 정리
        for i in range((now-1)//2, (home-1)//2+1):
            lst[i] += 1
            if mx < lst[i]:
                mx = lst[i]

    print(f'#{tc} {mx}')