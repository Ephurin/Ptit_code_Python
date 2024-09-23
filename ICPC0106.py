tetrad = {'00' : '0',
          '01' : '1',
          '10' : '2',
          '11' : '3'}

octal = {'000' : '0',
         '001' : '1',
         '010' : '2',
         '011' : '3',
         '100' : '4',
         '101' : '5',
         '110' : '6',
         '111' : '7'}

hexadecimal = {'0000' : '0',
               '0001' : '1',
               '0010' : '2',
               '0011' : '3',
               '0100' : '4',
               '0101' : '5',
               '0110' : '6',
               '0111' : '7',
               '1000' : '8',
               '1001' : '9',
               '1010' : 'A',
               '1011' : 'B',
               '1100' : 'C',
               '1101' : 'D',
               '1110' : 'E',
               '1111' : 'F'}

def to_tetard(binary):
    if len(binary) % 2 == 1: binary = '0' + binary
    mark = len(binary)
    ans = ''
    while mark != 0:
        ans = tetrad[binary[mark - 2: mark]] + ans
        mark -= 2
    return ans

def to_octal(binary):
    if len(binary) % 3 == 1: binary = '00' + binary
    if len(binary) % 3 == 2: binary = '0' + binary
    mark = len(binary)
    ans = ''
    while mark != 0:
        ans = octal[binary[mark - 3: mark]] + ans
        mark -= 3
    return ans

def to_hexadecimal(binary):
    if len(binary) % 4 == 1: binary = '000' + binary
    if len(binary) % 4 == 2: binary = '00' + binary
    if len(binary) % 4 == 3: binary = '0' + binary
    mark = len(binary)
    ans = ''
    while mark != 0:
        ans = hexadecimal[binary[mark - 4: mark]] + ans
        mark -= 4
    return ans

def solve():
    n =  int(input())
    binary =  input()
    if n == 2: print(binary)
    elif n == 4: print(to_tetard(binary))
    elif n == 8: print(to_octal(binary))
    elif n == 16: print(to_hexadecimal(binary))

if __name__=='__main__':
    for t in range(int(input())):
        solve()