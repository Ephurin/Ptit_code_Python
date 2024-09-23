def digitSum(n):
    tmp = 0
    for i in n:
        tmp += ord(i) - 48
    return str(tmp)

n = input()
ans = 0
while len(n) > 1:
    ans += 1 
    n = digitSum(n)
print(ans)