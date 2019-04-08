__author__ = 'dashik'

# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).


import random

N = 10
li = [random.randrange(-100, 100) for _ in range(N)]


def sort_bubble(array):
    n = 1
    while n < len(array):
        count = 0
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count = count + 1
        if count == 0:
            break
        else:
            n += 1
    return (array)
    # print (count)

print(li)
print (sort_bubble(li))