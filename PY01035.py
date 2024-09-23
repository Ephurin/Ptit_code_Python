conv2_8 = {'000' : '0',
           '001' : '1',
           '010' : '2',
           '011' : '3',
           '100' : '4',
           '101' : '5',
           '110' : '6',
           '111' : '7'}
string = input()
if len(string) % 3 == 1: string = '00' + string
elif len(string) % 3 == 2: string = '0' + string
mark = len(string) - 3
ans = ''
while True:
    ans = conv2_8[string[mark : mark + 3]] + ans
    if mark == 0: break
    mark -= 3
print(ans)