import sys
input = sys.stdin.readline
n, a, b = map(int, input().split())

if(a>b):
    temp = a
    a = b
    b = temp

if(a%2==1 and a+1==b):
    print(1)
elif(a==b):
    print(-1)
else:
  for i in range(2,n):
    if(a%2==0):
      a = a/2
    else:
      a = a//2 + 1

    if(b%2==0):
      b = b/2
    else:
      b = b//2 + 1
    
    if(a%2==1 and a+1==b):
      print(i)
      break