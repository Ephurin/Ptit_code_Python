def binarySearch(l, r, x, list):
    if l > r:
        return 'Not in sequence'
    m = (l + r) // 2
    if list[m] == x: return m + 1
    else:
        if list[m] < x: return binarySearch(m + 1, r, x, list)
        return binarySearch(l, m - 1, x, list)

list = []
N = 1e18
i = 1
while i <= N:
    j = 1
    while j <= N:
        k = 1
        while k <= N:
            list += [i * j * k]
            k *= 5
        j *= 3
    i *= 2
list.sort()

if __name__=="__main__":
    for t in range(int(input())):
        n = int(input())
        print(binarySearch(0, len(list), n, list))