di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
dii = [-1, -1, 1, 1]
djj = [-1, 1, -1, 1]

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [[0]*(n+m*2)]*m + [[0]*m + list(map(int, input().split())) + [0]*m for _ in range(n)] + [[0]*(n+m*2)]*m
    mx = 0
    for i in range(m-1, n+m):
        for j in range(m-1, n+m):
            sm1 = sm2 = arr[i][j]
            for k in range(1, m):
                for d in range(4):
                    sm1 += arr[i + di[d] * k][j + dj[d] * k]
                    sm2 += arr[i + dii[d] * k][j + djj[d] * k]
            if sm1 < sm2:
                sm = sm2
            else:
                sm = sm1
            if mx < sm:
                mx = sm

    print(f'#{tc} {mx}')