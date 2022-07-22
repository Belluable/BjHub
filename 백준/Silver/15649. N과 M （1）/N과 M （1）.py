from itertools import permutations
n, m = map(int, input().split())
data = list(range(1, n+1))
per = permutations(data,m)

for data_set in per:
    print(*data_set)