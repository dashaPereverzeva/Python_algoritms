__author__ = 'dashik'
# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
#A2 = 2*16^0 +10*16^1 = 2+160 = 162
#c4f = 15 +4*16 + 12*16*16 = 3151
#print (c4f)
# sum_ = 3151 + 162
# sum_=3313
# print(sum_)

from collections import deque


dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
addend1 = deque(input('Введите число в 16-ричной системе счисления '))
addend2 = deque(input('Введите число в 16-ричной системе счисления '))

#print(addend1)


def transform(my_deque):
    result = deque()
    for a in my_deque:
        if a.isdigit() == True:
            result.append(int(a))
        else:
            result.append(a)
    return (result)


addend1 = transform(addend1)
addend2 = transform(addend2)
# print (addend1)
# print(addend2)



dict_rev = {v: k for k, v in dict.items()}
#print (dict)

def change_val(list, dict):
    list_new = deque()
    for i in list:
        if i in dict.keys():
            list_new.append(dict[i])
        else:
            list_new.append(i)
    return (list_new)


addend1 = change_val(addend1, dict_rev)
addend2 = change_val(addend2, dict_rev)

d = len(addend1) - len(addend2)
if d > 0:
    for i in range(d):
        addend2.appendleft(0)
if d < 0:
    for i in range(-d):
        addend1.appendleft(0)

addend2.appendleft(0)
addend1.appendleft(0)

print(addend1, addend2)
addend1.reverse()
addend2.reverse()
print(addend1, addend2)

result = []
delta = 0
for i in range(len(addend1)):
    sum_ = addend1[i] + addend2[i] + delta
    if sum_ >= 16:
        element = sum_ % 16
        result.append(element)
        delta = sum_ // 16
    else:
        delta = 0
        result.append(sum_)
print(result)

result.reverse()
result = change_val(result, dict)
if result[0] == 0:
    result.popleft()

print(list(result))

