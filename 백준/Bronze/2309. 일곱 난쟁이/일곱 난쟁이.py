lst = []
for _ in range(9):
    lst.append(int(input()))
    
lst.sort()
n = sum(lst) - 100

for i in range(9):
    if n-lst[i] in lst:
        if lst[i] != n-lst[i] :
            lst.remove(n-lst[i])
            lst.remove(lst[i])
            break
        elif lst[i] == n-lst[i] and lst.count(lst[i]) >= 2:
            del lst[i+1]
            del lst[i]
            break
    
for h in lst:
    print(h)