<<<<<<< HEAD
a = input()
synonyms = dict()
for i in range(int(a)):
    b = input().split()
    synonyms[b[0]] = b[1]
    synonyms[b[1]] = b[0]
=======
a = input()
synonyms = dict()
for i in range(int(a)):
    b = input().split()
    synonyms[b[0]] = b[1]
    synonyms[b[1]] = b[0]
>>>>>>> 81637cdd51aa02d1df416edbd0bd3b51adc733cd
print(synonyms[input()])