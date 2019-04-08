__author__ = 'dashik'

line = 'papana'
list = []
i = 0
while i <= len(line):
    j = i + 1
    while j <= len(line):
        el = hash(line[i:j])
        # print (i, ":", j)
        # print(el)
        if el != hash(line) and el not in list:
            list.append(el)
        j = j + 1
    i = i + 1
# print(list)
print(len(list))

