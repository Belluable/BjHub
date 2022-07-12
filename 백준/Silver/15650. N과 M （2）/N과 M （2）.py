from itertools import combinations
n, m = map(int,input().split())
result = []
data = [i+1 for i in range(n)]
for i in combinations(data, m):
  result.append(i)
for j in result:
  print(*j)
