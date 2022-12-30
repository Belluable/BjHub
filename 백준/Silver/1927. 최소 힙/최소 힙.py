import heapq
import sys

input = sys.stdin.readline
hp = []
for _ in range(int(input())):
    k = int(input())
    if k == 0:
        if not hp:
            print(0)
        else:
            print(heapq.heappop(hp))
    else:
        heapq.heappush(hp, k)

