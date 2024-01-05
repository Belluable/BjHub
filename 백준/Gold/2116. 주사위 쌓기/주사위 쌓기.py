n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
dic = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}   # 주사위 짝짓기

ans = 6*n
sm = []
for start in range(1, 7):
    s = 0
    for i in range(n):
        idx_s = lst[i].index(start)
        if lst[i][idx_s] == 6 or lst[i][dic[idx_s]] == 6:
            s -= 1
            if lst[i][idx_s] == 5 or lst[i][dic[idx_s]] == 5:
                s -= 1
        start = lst[i][dic[idx_s]]

    sm.append(s)

print(ans+max(sm))