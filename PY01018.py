p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while(True):
    inin = input().split()
    if inin[0] == '0': break
    else:
        tmp = inin[1]
        dis = int(inin[0])
        list = []
        for c in tmp:
            for i in range(28):
                if c == p[i]:
                    c = p[(i+dis)%28]
                    list.append(c)
                    break
        list.reverse()
        for c in list: print(c,end='')
        print()