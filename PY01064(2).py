alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if __name__=='__main__':
    for t in range(int(input())):
        n, k = map(int, input().split())
        s = ''
        for i in range(n):
            s = s + alphabet[i] + s
        print(s[k - 1])