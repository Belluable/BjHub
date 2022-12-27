def solution(data, col, row_begin, row_end):
    answer = 0
    c = col-1
    row_b = row_begin-1
    row_e = row_end-1
    S = []
    
    data.sort(key=lambda x :(x[c], -x[0]))
    
    for i in range(row_b, row_end):
        s = 0
        for num in data[i]:
            s += num % (i+1)
        S.append(s)
    
    for s in S:
        answer ^= s
    
    return answer