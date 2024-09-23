def valid(a):
    for i in a:
        if int(i) < 0 or int(i) > 255: return False
    return len(a) == 4

def solve():
    n =  input()
    a = []
    tmp = ''
    for c in n:
        if c != '.':
            if c in '0123456789': tmp += c
            else: return 'NO'
        elif c != '.' : return 'NO'
        else: 
            a.append(tmp)
            tmp = ''
    if tmp != '': a.append(tmp)
    if valid(a): return 'YES'
    return 'NO'

if __name__=='__main__':
    for t in  range(int(input())):
        print(solve())