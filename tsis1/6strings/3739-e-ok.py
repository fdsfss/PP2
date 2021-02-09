s = input()
a = s.find('f')
b = s.rfind('f')
if a == -1:
    import sys
    sys.exit()
elif b == a or b == -1:
    print(a)
else:
    print(a, b, sep=' ')