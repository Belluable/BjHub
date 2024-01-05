ans = ['a', 'b', 'c', 'd']

for tc in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # d
    if p1<x2 or p2<x1 or q2<y1 or q1<y2:
        print(ans[3])
    elif (x2, q2) == (p1, y1) or (x2, y2) == (p1, q1) or (p2, y2) == (x1, q1) or (p2, q2) == (x1, y1):
        print(ans[2])
    elif (x2 == p1 or p2 == x1) and (y1 < q2 and y2 < q1):
        print(ans[1])
    elif (y1 == q2 or y2 == q1) and (x2 < p1 and x1 < p2):
        print(ans[1])
    else:
        print(ans[0])