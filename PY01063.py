def countSubString(str1, str2):
    l2 = len(str2)
    count, id = 0, str1.find(str2)
    while id != -1:
        count += 1
        id = str1.find(str2, id + l2)
    return count

for i in range(int(input())):
    str1 = input()
    str2 = input()
    print(countSubString(str1, str2))