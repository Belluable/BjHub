tc = int(input())
data = []
for i in range(tc):
  n = int(input())
  print("#", i+1, sep = "")
  for j in range(n):
    word, m = input().split()
    word = [word for _ in range(int(m))]
    data.extend(word)
    
j = 10
while j<len(data):
  data.insert(j, ' ')
  j += 11
answer = "".join(data).split()
print(*answer, sep = '\n')