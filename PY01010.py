for i in range (int(input())):
    string = input()
    if int(string[0]+string[1]) == int(string[-2]+string[-1]): print('YES')
    else: print('NO')