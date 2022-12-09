def solution(n,a,b):
    answer = 0
    for _ in range(n//2):
        answer += 1
        if (a+1)//2 == (b+1)//2:
            break
        else:
            a, b = (a+1)//2, (b+1)//2
    
    return answer