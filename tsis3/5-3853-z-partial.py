a = input().split()
k = int(input())

while k > len(a):
    k -= len(a)
while k <= 0:
    k += len(a) + 1
for i in range(k - 1, len(a)):
    print(a[i], end=' ')
for i in range(0, k - 1):
    print(a[i], end=' ')
