n, m = map(int, input().split())
lst = []
cnt = 0

for _ in range(n):
    lst.append(input())

for _ in range(m):
    if input() in lst:
        cnt += 1

print(cnt)