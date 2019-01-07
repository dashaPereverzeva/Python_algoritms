__author__ = 'dashik'
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

A = 10
array_max = 10
array = [random.randint(0, array_max) for _ in range(A)]
print(array)

num_max = array[0]
num_min = array[0]
item_min = 0
item_max = 0
for item, num in enumerate(array):
    if num > num_max:
        num_max = num
        item_max = item
    if num < num_min:
        num_min = num
        item_min = item

print('Наименьшее число ', array[item_min], 'наибольшее число - ', array[item_max])

sum = 0
if item_min < item_max:
    for item in array[item_min + 1: item_max]:
        sum = sum + item
if item_max < item_min:
    for item in array[item_max + 1: item_min]:
        sum = sum + item
print('Сумма эелементов между ними - ', sum)
