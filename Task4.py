__author__ = 'dashik'
# Определить, какое число в массиве встречается чаще всего.

import random

A = 10
ARRAY_MAX = 7
array = [random.randint(0, ARRAY_MAX) for _ in range(A)]
print(array)
count_max = 0
max_number = 0
for array_element in array:
    count = 0
    for num in array:
        if num == array_element:
            count = count + 1
        if count > count_max:
            count_max = count
            max_number = num

print('Число', max_number, 'встречается', count_max, 'раз(а)')





