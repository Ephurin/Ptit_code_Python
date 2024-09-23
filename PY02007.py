ll = []
while len(ll) < 10:
    a = input()
    if a == '': break
    else: ll += [int(i) for i in a.split()]
ans = []
for i in range(10):
    ans.append(ll[i] % 42)
ans = list(set(ans))
print(len(ans))