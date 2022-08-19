import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]

    arr[x][y] = 0
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 < nx < h+1 and 0 < ny < w+1 and arr[nx][ny] == 1:
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [[0]*(w+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(h)] + [[0]*(w+2)]
    cnt = 0

    for i in range(1, h+1):
        for j in range(1, w+1):
            if arr[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)