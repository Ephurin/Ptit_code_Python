def crackSum(n):
    tmp = str(n)
    l = len(tmp) // 2
    tmp = int(tmp[:l]) + int(tmp[l:])
    return tmp

if __name__=='__main__':
    n = int(input())
    while n > 9:
        n = crackSum(n)
        print(n)