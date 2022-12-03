def change(a):
    return (a+1) % 2


n = int(input())
lst = [0] + list(map(int, input().split())) + [0]
std = int(input())

for _ in range(std):
    sex, num = map(int, input().split())
    if sex == 1:    # male
        i = 1
        while num * i <= n:
            n_num = num * i
            lst[n_num] = change(lst[n_num])
            i += 1

    elif sex == 2:  # female
        i = 0
        while num-i >= 1 and num+i <= n:
            if lst[num-i] == lst[num+i]:
                i += 1
            else:
                break
        i -= 1

        for k in range(num - i, num + i+1):
            lst[k] = change(lst[k])

for i in range(1, n+1):
    if i % 20 == 0:
        print(lst[i])
    else:
        print(lst[i], end=" ")
