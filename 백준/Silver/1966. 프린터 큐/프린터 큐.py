from collections import deque
import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
  n, m = map(int, input().split())
  data = list(map(int, input().split()))
  target = [0 for _ in range(n)] 
  target[m] = 1 

  cnt =0
  while True:
    if data[0] == max(data):
      cnt += 1
      if target[0] == 1:
        print(cnt)
        break
      else:
        del data[0]
        del target[0]

    else:
      data.append(data[0])
      target.append(target[0])
      del data[0]
      del target[0]