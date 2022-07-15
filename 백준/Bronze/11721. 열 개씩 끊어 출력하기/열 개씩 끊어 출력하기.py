word = list(input().strip())
i = 10
while i<len(word):
  word.insert(i, ' ')
  i += 11
data = "".join(word).split()
print(*data, sep = '\n')