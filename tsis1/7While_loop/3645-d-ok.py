a = int(input())
n = 1
k = bool(0)
while n <= a:
    if n == a:
        k = 1
    n *= 2
print("YES") if k == 1 else print("NO")
