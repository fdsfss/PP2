<<<<<<< HEAD:tsis3/5-3853-z-partial.py
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
=======
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
>>>>>>> 81637cdd51aa02d1df416edbd0bd3b51adc733cd:tsis3/5-3853-z.py
