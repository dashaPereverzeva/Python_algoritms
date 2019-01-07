__author__ = 'dashik'
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

A = 10
array_max = 100
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
array[item_max] = num_min
array[item_min] = num_max
print(array)

