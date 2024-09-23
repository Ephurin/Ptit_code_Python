posChar = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM._'
def valid(n):
    for c in n:
        if c not in posChar: return 'no'
    l = len(n)
    if n[l-3:] not in '.py .Py .pY .PY'.split(): return 'no'
    return 'yes'

string = input()
print(valid(string))