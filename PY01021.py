for t in range(int(input())):
    s = input()
    sum = 0
    a = []
    for i in range(len(s)):
        if s[i] in '0123456789':
            sum += int(s[i])
        else: a.append(s[i])
    a.sort()
    ans = ''
    for i in a: ans += i
    ans += str(sum)
    print(ans)