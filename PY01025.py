string = input()
t = len(string)-1
while t >=3:
    t -= 2
    string = string[:t] + ',' + string[t:]
    t -= 1
print(string)