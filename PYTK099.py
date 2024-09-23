fi1 = open('DATA1.in', 'r')
fi2 = open('DATA2.in', 'r')
a, b = [], []
for x in fi1:
    x = x.lower()
    a += x.split()
for x in fi2:
    x = x.lower()
    b += x.split()
a = list(set(a))
b = list(set(b))
for i in sorted(a):
    if i not in b: print(i, end = ' ')
print()
for i in sorted(b):
    if i not in a: print(i, end = ' ')
fi1.close()
fi2.close()