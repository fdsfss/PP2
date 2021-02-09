a = int(input())
n = 1
k = 0
if a == 1:
    print(0)
else:
    while n * 2 < a:
        n *= 2
        k += 1
    print(k + 1)