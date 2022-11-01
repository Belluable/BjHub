def dfs(i, j, num):
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    num += arr[i][j]

    if len(num) == 6:
        lst.add(num)
        return
    else:
        for k in range(4):
            if 0 <= i + di[k] < 5 and 0 <= j + dj[k] < 5:
                ni, nj = i + di[k], j + dj[k]
                dfs(ni, nj, num)


arr = [list(input().split()) for _ in range(5)]
lst = set()
num = ''
for i in range(5):
    for j in range(5):
        dfs(i, j, num)

print(len(lst))