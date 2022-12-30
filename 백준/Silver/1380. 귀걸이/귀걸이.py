i = 1
while True:
    n = int(input())
    if n == 0:  break

    std = []
    for _ in range(n):
        std.append(input())

    nums = [-1]*n

    for _ in range(2*n-1):
        num, alpha = input().split()
        num = int(num)
        nums[num-1] *= -1

    for k in range(n):
        if nums[k] == 1:
            print(i, std[k])
            i += 1
            break

