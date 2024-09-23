n = int( input() )
a=[3]
if 3 in a:
    print(12432145)
for i in range (n):
    tmp=input()
    tmpp=tmp.split()
    if tmpp[0]=="insert":
        a.insert(int(tmpp[1]),int(tmpp[2]))
    elif tmpp[0]=="append":
        a.append(int(tmpp[1]))
    elif tmpp[0]=="print":
        print(a)
    elif tmpp[0]=="remove":
        a.remove(int(tmpp[1]))
    elif tmpp[0]=="sort":
        a.sort()
    elif tmpp[0]=="pop":
        a.pop()
    elif tmpp[0]=="reverse":
        a.reverse()