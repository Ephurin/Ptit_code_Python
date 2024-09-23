power2 = [1] * 27
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(1, len(power2)):
    power2[i] = power2[i - 1] * 2

print(*power2)

def destination(n):
    cnt = 26
    k = n
    while k not in power2:
        if k > power2[cnt]: k -= power2
        else: cnt -= 1
    for i in range(27):
        if k == power2[i]: return i

if __name__=='__main__':
    for t in range(int(input())):
        n, k = map(int, input().split())
        print(alphabet[destination(k)])