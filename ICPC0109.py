MAX = int(1e8)

for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    first_min, second_min, third_min = MAX, MAX, MAX
    for i in a:
        if i < first_min:
            third_min = second_min
            second_min = first_min
            first_min = i
        elif i < second_min:
            third_min = second_min
            second_min = i
        elif i < third_min:
            third_min = i

    print(first_min + second_min + third_min)