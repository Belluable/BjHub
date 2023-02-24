n = int(input())
arr = [[0]*1002 for _ in range(1002)]
ans = 0
for num in range(1, n+1):
    x1, y1, w, h = map(int, input().split())
    for i in range(w):
        for j in range(h):
            arr[x1 + i][y1 + j] = num

ans = [0]*n

for lst in arr:
    if lst:
        for num in range(n):
            ans[num] += lst.count(num+1)

for s in ans:
    print(s)