import math

n = int(input())
def minus(n):
  if n == 0 or n == 1:
    return str(n)
  if n % 2:
    return minus((n-1) // (-2)) + minus(abs(n % (-2)))
  else:
    return minus(n // (-2)) + minus(abs(n % (-2)))

print(minus(n))