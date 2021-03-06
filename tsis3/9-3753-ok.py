<<<<<<< HEAD
a = input().split()
b = set()
c = set()
for i in range(int(a[0])):
    b.add(input())
for i in range(int(a[1])):
    c.add(input())
print(len(b.intersection(c)))
print(*sorted(b.intersection(c), key=int))
print(len(b.difference(c)))
print(*sorted(b.difference(c), key=int))
print(len(c.difference(b)))
=======
a = input().split()
b = set()
c = set()
for i in range(int(a[0])):
    b.add(input())
for i in range(int(a[1])):
    c.add(input())
print(len(b.intersection(c)))
print(*sorted(b.intersection(c), key=int))
print(len(b.difference(c)))
print(*sorted(b.difference(c), key=int))
print(len(c.difference(b)))
>>>>>>> 81637cdd51aa02d1df416edbd0bd3b51adc733cd
print(*sorted(c.difference(b), key=int))