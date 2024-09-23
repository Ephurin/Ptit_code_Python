s1 = input()
s2 = input()
des = int(input()) - 1
s1 = s1[0:des] + s2 + s1[des:]
print(s1)