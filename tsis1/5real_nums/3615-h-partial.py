p = int(input())
x = int(input())
y = int(float(input()))
m = x + y / 100
first = m / 100 * (100 + p)
second = int((first - int(first)) * 100 % 100)
print(str(int(first)) + " " + str(second))
