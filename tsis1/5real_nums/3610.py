import math

a = float(input())
if int(a * 10 % 10) >= 5:
    print(math.ceil(a))
else:
    print(math.floor(a))