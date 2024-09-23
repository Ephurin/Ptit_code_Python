def convert(s):
    a = []
    mark = -1
    ans = ''
    for i in s:
        a.append(int(i))
    for i in range(len(a) - 2, -1, -1):
        if a[i] > a[i + 1]:
            mark = i
            for j in range(len(a) - 1, -1, -1):
                if a[j] < a[i - 1]:
                    a[j], a[i - 1] = a[i - 1], a[j]
                    break
            break
    if mark == -1: return -1
    if a[0] == 0: return -1
    b = sorted(a[mark:], reverse=True)
    for i in range(mark):
        ans += str(a[i])
    for i in b:
        ans += str(i)
    return ans

if __name__=='__main__':
    for t in range(int(input())):
        s = input()
        ans = convert(s)
        print(ans)