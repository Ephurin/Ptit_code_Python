for t in range(int(input())):
    s = input()
    if len(s) > 100:
        if s[100] == ' ': s = s[:100]
        else: s = s[:100]
        while s[-1] != ' ': s = s[:-1] 
    print(s)