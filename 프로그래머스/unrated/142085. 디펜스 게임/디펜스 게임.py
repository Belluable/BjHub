# def solution(n, k, enemy):
#     answer = 0
    
#     if k >= len(enemy) or n >= sum(enemy):
#         answer = len(enemy)
        
#     else:
#         for i in range(len(enemy)):
#             if n < enemy[i]:
#                 if k == 0:
#                     answer = i
#                     break
#                 else:
#                     k -= 1
#             else:
#                 n -= enemy[i]

#             answer = i+1

#     return answer

import heapq as hq
def solution(n, k, enemy):
    l=[]
    s=0
    for i in range(len(enemy)):
        hq.heappush(l,-enemy[i])
        s+=enemy[i]
        if s>n:
            if k>0:
                k=k-1
                s+=hq.heappop(l)
            else:
                i=i-1
                break
    return i+1