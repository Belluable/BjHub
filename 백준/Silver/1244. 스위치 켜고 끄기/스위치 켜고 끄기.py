def change(a):
    lst[a] = (lst[a]+1) % 2
    return


n = int(input())
lst = [0] + list(map(int, input().split()))
std = int(input())

for _ in range(std):
    sex, num = map(int, input().split())
    if sex == 1:    # male
        for i in range(num, n+1, num):
            change(i)

    elif sex == 2:  # female
        change(num)

        for i in range(n//2):
            if num+i > n or num-i < 1:
                break
            if lst[num-i] == lst[num+i]:
                change(num-i)
                change(num + i)
            else:
                break

for i in range(1, n+1):
    if i % 20 == 0:
        print(lst[i])
    else:
        print(lst[i], end=" ")
