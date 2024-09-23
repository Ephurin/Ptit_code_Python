if __name__=='__main__':
    for t in range(int(input())):
        s = input()
        tmp = 1
        ans = ''
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]: tmp += 1
            else: 
                ans += (str(tmp) + s[i])
                tmp = 1
        ans += (str(tmp) + s[-1])
        print(ans)