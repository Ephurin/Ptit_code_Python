inp = input()
if ":" in inp:
    inp = inp.split(':')[1]
h, m, s = map(int, inp.split())

tick = (h*3600 + m*60 + s) % (12*3600)
angle_per_tick = 360 / (12*3600)
angle = (h*30 + m*0.5 + s*(1/120)) / 360 * 360

print('Angle:',angle)