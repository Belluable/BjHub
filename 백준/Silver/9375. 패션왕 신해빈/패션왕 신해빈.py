for tc in range(int(input())):
    n = int(input())
    wear = []
    for i in range(n):
        _, w = input().split()
        wear.append(w)

    lst = list(set(wear))
    ans = 1
    for i in lst:
        ans *= (wear.count(i)+1)

    print(ans-1)