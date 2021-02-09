s = input()
b = int(len(s) / 2)
if len(s) % 2 != 0:
    b += 1
print(s[b:], s[:b], sep = '')