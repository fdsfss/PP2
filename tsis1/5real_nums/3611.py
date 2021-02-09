a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
from math import sqrt
print(sqrt(p * (p - a) * (p - b) * (p - c)))
