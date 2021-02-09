degree = float(input())
H = int(degree // 30)
M = (degree - float(H) * 30) * 2 * float(H)
print(int(M))