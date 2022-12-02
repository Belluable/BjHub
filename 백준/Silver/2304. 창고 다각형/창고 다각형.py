n = int(input())
dct = {}
for _ in range(n):
    a, b = map(int, input().split())
    dct[a] = b

lst = dict(sorted(dct.items()))
lst_dec = dict(sorted(dct.items(), reverse=True))
m = max(dct.values())

ans = 0
n_key = n_val = 0
for key, val in lst.items():
    ans += (key-n_key) * (n_val)

    if val == m:
        key_l = key
        break
    else:
        if n_val < val:
            n_val = val
    n_key = key


n_key, n_val = 1000, 0
for key, val in lst_dec.items():
    ans += (n_key-key) * (n_val)
    if val == m:
        key_r = key+1
        break
    else:
        if n_val < val:
            n_val = val
    n_key = key


ans += (key_r - key_l) * m

print(ans)




