a = int(input())
k = 0
for i in range(2, int(a / 2)):
    for j in range(2, i):
        if i % j == 0:
            continue
        k = 0
        print(i)
        break