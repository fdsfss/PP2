x = float(input())
y = float(input())
day = 0
if x == y:
    print(0)
else:
    while x < y:
        x *= 1.1
        day += 1
    print(day + 1) if x > y else print(day)
