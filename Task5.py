__author__ = 'dashik'
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

A = 10
ARRAY_MAX = 100
ARRAY_MIN = -100
array = [random.randint(ARRAY_MIN, ARRAY_MAX) for _ in range(A)]
print(array)

element_neg = 0
element_max_neg = ARRAY_MIN

for num in array:
    if num < 0:
        element_neg = num
        if element_neg > element_max_neg:
            element_max_neg = element_neg
if element_neg == 0:
    print('В вашем массиве нет ни одного отрицательного числа')
else:
    print('Максимальный отрицательный элемент - ', element_max_neg)