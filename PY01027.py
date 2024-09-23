def valid(n):
    if n[0] == '8': return 'NO'
    for c in n:
        if c not in '68': return 'NO'
    if n.find('888') == -1: return 'YES'
    return 'NO'
string = input()
print(valid(string))
