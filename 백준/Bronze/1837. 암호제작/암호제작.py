n, k = map(int, input().split())

def pw(n, k):
  for i in range(2,k):
    if n%i == 0:
      return f'BAD {i}'
      break

if pw(n, k) == None:
  print('GOOD')
else:
  print(pw(n, k))