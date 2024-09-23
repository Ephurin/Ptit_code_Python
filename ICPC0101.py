n = int(input())
num_list = [int(i) for i in input().split()]
i = 1
while i < len(num_list):
    if (num_list[i] + num_list[i-1]) % 2 == 0:
        num_list.pop(i)
        num_list.pop(i-1)
        if i> 1: i -= 1
    else: i += 1

print(len(num_list))