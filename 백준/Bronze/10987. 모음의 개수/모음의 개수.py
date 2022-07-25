str = input().strip()
vowel = 'aeiou'
cnt = 0
for v in vowel:
    cnt += str.count(v)
print(cnt)