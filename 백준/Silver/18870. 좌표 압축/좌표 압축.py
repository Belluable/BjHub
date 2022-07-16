n = int(input())
arr = list(map(int, input().split()))

arr2 =list(sorted(set(arr)))
arr2 = {arr2[i] : i for i in range(len(arr2))}
print(*[arr2[i] for i in arr])