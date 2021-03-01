'''
a = set(input().split())
b = set(input().split())
z = b.intersection(a)
print(len(z))
'''
print(len(set(input().split()).intersection(set(input().split()))))
# print(len(set(input().split()) & set(input().split())))