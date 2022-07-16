n, m = map(int,input().split())
price1 = []
price2 = []
price3 = []
price4 = []
for i in range(m):
  six, one = map(int,input().split())
  price1.append(n%6*one)
  price2.append(n//6*six)
  price3.append((n//6+1)*six)
  price4.append(n*one)
print(min(min(price1)+min(price2), min(price3), min(price4)))