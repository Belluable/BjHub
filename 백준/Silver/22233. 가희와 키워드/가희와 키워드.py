import sys
input = sys.stdin.readline

n, m = map(int, input().split())
kw = {}
cnt = 0
for _ in range(n):
    kw[input().rstrip()] = 0

for _ in range(m):
    arti = input().rstrip().split(',')

    for k in arti:
        if k in kw.keys():
            if kw[k] == 0:
                cnt += 1
                kw[k] = 1

    print(n-cnt)