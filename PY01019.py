def check(a, b):
    for i in range(len(a)):
        if abs(ord(a[i]) - ord(a[i - 1])) != abs(ord(b[i]) - ord(b[i - 1])):
            return 'NO'
    return 'YES' 

for t in range(int(input())):
    string = input()
    print(check(string, string[::-1]))