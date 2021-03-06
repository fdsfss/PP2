import re

f = open('data.txt', 'r')
data = f.read()

name = re.search(r'Филиал\sТОО\s\w+\s\w+', data)

print(name)
#print("1. Name of the company: " + name.group())
