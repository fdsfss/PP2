def IsPointInSquare(x, y):
    return x <= y + 1 and x >= y - 1 and y <= -x + 1 and y >= -x - 1

if IsPointInSquare(float(input()), float(input())) == 1:
    print("YES")
else:
    print("NO")