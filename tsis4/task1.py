import re

f = open('./data.txt', 'r', encoding='utf-8')
data = f.read()

name = re.search(r'Филиал\sТОО\s\w+\s\w+', data)
BIN_number = re.search(r'\d{12}', data)
items = re.findall(r'\d+\.\n(.*)', data)
cnt = re.findall(r'(\d),\d{3}', data)
price = re.findall(r'x\s([\d\s]+,\d{2})\n', data)
t_price = re.findall(r'\n([\d\s]+,\d{2})\n', data)
date = re.search(r'\d{2}\.\d{2}\.\d{4}\s\d{2}\:\d{2}\:\d{2}', data)
# 18.04.2019 11:13:58
address = re.search(r'\w+\.\s[\w+\-]+\,\w+\,[\s\w+]+\,\d{2}\,\s\w+\-\d', data)
# г. Нур-султан,Казахстан, Мангилик Ел,19, нп-5

print("1. Name of the company: " + name.group())
print("2. BIN number: " + BIN_number.group())

for i in range(len(items)):
    # print(i+1)
    print("1. Title —— (" + items[i] + ")")
    print("2. Cout —— (" + cnt[i] + ")")
    print("3. Unit price —— (" + price[i] + ")")
    print("4. Total price —— (" + t_price[i] + ")")

print("4. Date —— (" + date.group() + ")")
print("5. Address ——" + address.group() + ")")