string = input()
lower_count, upper_count = 0, 0
for c in string:
    if c.islower(): lower_count += 1
    else: upper_count += 1

if lower_count < upper_count: string = string.upper()
else: string = string.lower()

print(string)