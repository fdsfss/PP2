x = float(input())
p = float(input()) / 100
y = int(input())
years = 0
while int(x) < y:
    print(type(x))
    x *= 1 + p
    years += 1
print(years)