x = float(input())
p = float(input()) / 100
y = int(input())
years = 0
while int(x) < y:
    x *= 1 + p
    years += 1
    # x = int(x)
print(years)