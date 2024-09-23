import sys
fi = open('input')
fo = open('output', 'w', encoding = 'utf-8')
sys.stdin = fi
sys.stdout = fo

a, b = map(int, input().split())
k = b - a
ans = b - k * (k + 1) // 2
print(ans)

fi.close()
fo.close()