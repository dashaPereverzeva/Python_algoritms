__author__ = 'dashik'
from collections import deque
import collections, itertools


dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
addend1 = deque(input('Введите число в 16-ричной системе счисления '))
addend2 = deque(input('Введите число в 16-ричной системе счисления '))


def transform(my_deque): # заменяет строки с числами на числа
    result = deque()
    for a in my_deque:
        if a.isdigit() == True:
            result.append(int(a))
        else:
            result.append(a)
    return (result)


def change_val(list, dict): # буквенные обозначения переводит в численные
    list_new = deque()
    for i in list:
        if i in dict.keys():
            list_new.append(dict[i])
        else:
            list_new.append(i)
    return (list_new)


addend1 = transform(addend1) # заменили строки с числами на числа
addend2 = transform(addend2)


dict_rev = {v: k for k, v in dict.items()} # "перевернули словарь" - ключ -- значение

addend1 = change_val(addend1, dict_rev) # заменили буквенные обозначения числами
addend2 = change_val(addend2, dict_rev)

print(addend1, addend2)


d = len(addend1) - len(addend2) # добавляем нули в начало множителей так, чтобы их длина стала одинаковой и плюс еще
                                # один дополнительный ноль к обоим множителям , чтобы корректно выполнять вычисления
if d > 0:
    for i in range(d+1):
        addend2.appendleft(0)
    addend1.appendleft(0)
if d < 0:
    for i in range(-d - 1):
        addend1.appendleft(0)
    addend2.appendleft(0)
print(addend1, addend2)

addend1.reverse() # "Переворачиваем" множители так, чтобы начинать арифметическое действие с первого элемента списка
addend2.reverse()

print(addend1, addend2)

result_all = deque()# выполняем умножение в столбик, в итоге получаем матрицу, элементы которой далее надо будет сложить
result = deque()
delta = 0
for i in addend2:
    result = []
    for j in addend1:
        mult = i * j + delta
        if mult >= 16:
            delta = mult // 16
            result.append(mult - (mult // 16) * 16)
        else:
            delta = 0
            result.append(mult)
    result_all.append(result)

print(result_all)

result_all.reverse()# переворачиваем матрицу, для того, чтобы было удобней убрать списки, все эдементы которых равны 0.

sum_ = 0
for j in range(0, len(result_all)): # убираем списки, все эелементы которых равны 0
    for i in result_all[j]:
        sum_ = sum_ + i
    if sum_ != 0:
        result_all = deque(itertools.islice(result_all, j, len(result_all)))
        break

result_all.reverse() # обратно переворачиваем матрицу
print(result_all)

result_all_new = deque() # добавляем в каждое слагаемое слева и справа необходимое количество нулей, чтобы далее корректно
                        # выполнять их сложение
k = len(result_all) - 1
m = 0
for i in result_all:
    for j in range(k+1):
        i.append(0)
    for j in range(m):
        i.insert(0, 0)
    result_all_new.append(i)
    m = m + 1
    k = k - 1

print(result_all_new)

result = [] # Выполняем поэелементно сложение
delta = 0
sum_ = 0
i = 0
while i < len(result_all_new[0]):
    for j in result_all_new:
        sum_ = sum_ + j[i]
    sum_ = sum_ + delta
    if sum_ >= 16:
        # element = sum_ - 16
        element = sum_ % 16
        result.append(element)
        delta = sum_ // 16
    else:
        delta = 0
        result.append(sum_)
    i = i + 1
    sum_ = 0
print(result)

result.reverse() #  Поворачиваем полученный список
result = change_val(result, dict) # заменяем числовые значения на буквенные
if result[0] == 0: # убираем лишние нули
    result.popleft()

print(list(result))# выводим ответ