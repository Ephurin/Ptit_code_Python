def valid(a, n):
    sum = 0
    for i in n:
        sum += a[int(i)]
    if int(n) == sum: return 'Yes'
    return 'No'

def solve(a):
    n = input()
    print(valid(a, n))

if __name__=='__main__':
    kri = [1] * 10
    for i in range(1, 10):
        kri[i] = kri[i - 1] * i
    for t in range(int(input())):
        solve(kri)