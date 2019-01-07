
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
import random

list_result = [0]*8
index = 0
for k in range(2, 10):
    for i in range(2, 100):
        if i % k == 0:
            list_result[index] = list_result[index] + 1
    index = index + 1
i = 0
for item in range(2, 10):
    print('Количество чисел в диапазоне от 2 до 99, кратных ', item, '-', list_result[i])
    i = i + 1


