n, l = map(int, input().split())
lst = list(map(int, input().split()))
arr = [0] * 1001
ans = 0

for i in lst:
    arr[i] = 1

if l == 1:
    ans = n
else:
    i = 1
    while i <= 1000:
        if arr[i] == 1:
            ans += 1
            i += l
        else:
            i += 1
        if ans == n:
            break

print(ans)
