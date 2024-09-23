import math

t = int(input())
for i in range (t):
    cur_mon, per, aim_mon = map(float,input().split())
    per /= 100
    per += 1
    times = aim_mon/cur_mon
    ans = math.ceil(math.log(times, per))
    print(ans)