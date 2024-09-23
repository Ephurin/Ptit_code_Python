m, v, t, d = int(input()), int(input()), int(input()), input()
ans = (v * t) % m
if d == 'A': ans = m - ans
print(ans)