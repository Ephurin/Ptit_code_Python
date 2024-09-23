if __name__=='__main__':
    for t in range(int(input())):
        s = input()
        a = []
        tmp = ''
        for i in s:
            if i in '0123456789': tmp += i
            elif tmp != '':
                a.append(int(tmp))
                tmp = ''
        a.sort()
        print(a[len(a) - 1])