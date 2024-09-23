def valid(n):
    if str(n) != str(n)[::-1]: return False
    if len(str(n)) % 2 == 1: return False
    for i in str(n):
        if i not in '2 4 6 8 0'.split():
             return False
    return True

if __name__=='__main__':
    for t in range(int(input())):
        n = int(input())
        for i in range(22, n ):
            if valid(i): print(i, end = ' ')
        print()