import os

text = 'wfgrwhgetshetheheheh\n'

with open('text.txt','w') as file:
    for i in range (1000):
        file.write(text)
