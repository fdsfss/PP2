s = 1
for i in range(1, 9 + 1):
    s += (-1) ** i * 1 / (1 + 2 * i)
s *= 4
print(s)
