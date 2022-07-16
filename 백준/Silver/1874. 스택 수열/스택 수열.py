import sys
input = sys.stdin.readline
n = int(input())

arr1 = []
arr2 = []
num = 1
flag = 1

for i in range(n):
    data = int(input())
    while num <= data:
        arr1.append(num)
        arr2.append("+")
        num = num + 1
    if arr1[-1] == data:
        arr1.pop()
        arr2.append("-")
    else:
        flag = 0
if flag == 0:
    print("NO")
else:
    for i in arr2:
        print(i)