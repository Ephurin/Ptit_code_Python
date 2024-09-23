def conv(a, n):
    if a == 10: return str(n)
    else:
        tmp = ''
        while n > 0:
            tmp = str(n % a) + tmp
            n //= a
        return tmp if tmp != '' else '0'

def valid(n):
    return n == n[::-1]

while True:
    s = input()
    if s == '-1': break
    a, b, c = map(int, s.split())
    x = conv(b, a)
    y = conv(c, a)
    if valid(x) and valid(y) : print('YES')
    else: print('NO')
