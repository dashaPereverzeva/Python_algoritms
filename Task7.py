__author__ = 'dashik'
# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
import random

A = 10
array_max = 10
array = [random.randint(0, array_max) for _ in range(A)]
print(array)

num_min1 = A
num_min2 = A

for num in array:
    if num <= num_min1 and num <= num_min2:
        num_min2 = num_min1
        num_min1 = num
    if num > num_min1 and num <= num_min2:
        num_min2 = num
print('Два наименьших элемента - ', num_min1,',', num_min2)