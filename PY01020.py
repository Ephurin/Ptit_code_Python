for i in range (int(input())):
    string = input()
    l = len(string)
    if string[l - 1] == '6' and string[l - 2] == '8': print('YES')
    else: print('NO')