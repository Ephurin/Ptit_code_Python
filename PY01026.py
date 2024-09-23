def reshape(a, b):
    if len(a) != len(b): return 'NO'
    else:
        for i in a:
            if a.count(i) != b.count(i): return 'NO'
    return 'YES'

if __name__=='__main__':
    for i in range(int(input())):
        a = input()
        b = input()
        print('Test {}: {}'.format(i + 1, reshape(a, b)))