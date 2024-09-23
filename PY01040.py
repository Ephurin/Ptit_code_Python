Char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Dict = {}
for i in range(26):
    Dict[Char[i]] = i

def devide(s):
    k = len(s) // 2
    first_half = s[ : k]
    second_half = s[k : ]
    return [first_half, second_half]

def rotate(s):
    tmp = 0
    ss = ''
    for i in s:
        tmp += Dict[i]
    for i in s:
        k = (Dict[i] + tmp) % 26
        ss += Char[k]
    return ss

def merge(a, b):
    ans = ''
    for i in range(len(a)):
        k = (Dict[a[i]] + Dict[b[i]]) % 26
        ans += Char[k]
    return ans

if __name__=='__main__':
    for t in range(int(input())):
        s = input()
        s.upper()
        k = devide(s)
        a, b = rotate(k[0]), rotate(k[1])
        ans = merge(a, b)
        print(ans)
