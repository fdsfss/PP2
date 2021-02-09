def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1

if IsPointInSquare(float(input()), float(input())) == 1:
    print("YES")
else:
    print("NO")