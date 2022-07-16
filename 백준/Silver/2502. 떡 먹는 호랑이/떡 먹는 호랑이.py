import sys
input = sys.stdin.readline
day, total = map(int,input().split())

def fibo(n):
    if n==0: return 0
    elif n==1: return 1
    else : 
        return fibo(n-1)+fibo(n-2)

x = fibo(day-2)
y = fibo(day-1)
for a in range(1, total):
  b = (total - x*a)/y
  if (float.is_integer(b) == True and a<=b):
    print(a)
    print(int(b))
    break