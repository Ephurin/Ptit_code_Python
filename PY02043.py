if __name__=='__main__':
    for i in range(int(input())):
        a = input()
        b = input()
        l = len(b)
        ans, ps = 0, 0
        while(ps < len(a) - l + 1):
            if a[ps : ps + l] == b: 
                ans += 1
                ps += l
            ps += 1
        print(ans)