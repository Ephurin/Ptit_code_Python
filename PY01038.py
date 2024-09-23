for i in range(int(input())):
    n = int(input())
    if n % 7 == 0: print(n)
    else:
        for i in range(1000):
            n += int(str(n)[::-1])
            if n % 7 == 0: 
                print(n)
                break
            