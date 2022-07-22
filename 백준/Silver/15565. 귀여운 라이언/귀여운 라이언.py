n, k = map(int,input().split())
lion = list(map(int, input().split()))
lion_id = dict(enumerate(lion))
num = []

for key, value in lion_id.items():
  if value == 1:
    num.append(key)

if k > len(num):
  print(-1)
else:
  min_lion = []
  i = 0
  while i <= len(num)-k:
    min_lion.append(num[i+k-1]-num[i]+1)
    i += 1
  print(min(min_lion))