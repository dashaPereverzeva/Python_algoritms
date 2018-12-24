__author__ = 'dashik'
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
n = int(input('Введите натуральное число: '))
summa = 1
next_el = 1
for i in range(n):
    next_el = next_el/(-2)
    summa = summa + next_el
    #print (next_el)
print (summa)