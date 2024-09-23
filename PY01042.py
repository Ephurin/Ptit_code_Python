def valid(n):
    for c in n:
        if c.isalpha():
            return 'NO'
        else:
            if int(c) >= 3: return 'NO'
    return 'YES'

for i in range(int(input())):
    string = input()
    print(valid(string))