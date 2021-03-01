a = input()
synonyms = dict()
for i in range(int(a)):
    b = input().split()
    synonyms[b[0]] = b[1]
    synonyms[b[1]] = b[0]
print(synonyms[input()])