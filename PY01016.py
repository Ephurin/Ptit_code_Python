for i in range(int(input())):
    string = input()
    ans = ''
    for i in range(len(string)):
        if string[i].isdigit():
           ans += string[i-1] * int(string[i])

    print(ans) 