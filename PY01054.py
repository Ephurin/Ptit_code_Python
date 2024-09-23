def digitTimes(n):
    tmp = 1
    for c in n:
        if c != '0':
            tmp *= int(c)
    return tmp

for t in range(int(input())):
    string = input()
    print(digitTimes(string))