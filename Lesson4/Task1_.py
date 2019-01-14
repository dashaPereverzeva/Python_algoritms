__author__ = 'dashik'
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.



import random
import sys
import cProfile

# # Вариант1: цикл
def test1(array_size):
    max_number = 100
    array = [random.randint(0, max_number) for _ in range(array_size)]
    # print(array)
    num_max = array[0]
    num_min = array[0]
    index_min = 0
    index_max = 0
    for item, num in enumerate(array):
        if num > num_max:
            num_max = num
            index_max = item
        if num < num_min:
            num_min = num
            index_min = item
    array[index_max] = num_min
    array[index_min] = num_max
    return (array)

# print(test1(10))
# 100 loops, best of 3: 44.7 usec per loop - 10
#100 loops, best of 3: 414 usec per loop - 100
#100 loops, best of 3: 7.51 msec per loop - 1000
#100 loops, best of 3: 83.7 msec per loop - 10000

#1 0.000    0.000    0.000    0.000 Task1_.py:10(test1) - 10
#1 0.000    0.000    0.001    0.001 Task1_.py:10(test1) - 100
#1 0.000    0.000    0.007    0.007 Task1_.py:10(test1) - 1000

#__________________________________________________________________________________________________________________

# Вариант2: рекурсия
#sys.getrecursionlimit()
sys.setrecursionlimit(2000)


def array_max(array):
    array_copy = array.copy()
    if len(array_copy) == 1:
        return (array_copy[0])
    if array_copy[0] >= array_copy[1]:
        array_copy.remove(array_copy[1])
        return array_max(array_copy)
    if array_copy[1] > array_copy[0]:
        array_copy.remove(array_copy[0])
        return array_max(array_copy)


def array_min(array):
    array_copy = array.copy()
    if len(array_copy) == 1:
        return (array_copy[0])
    if array_copy[0] >= array_copy[1]:
        array_copy.remove(array_copy[0])
        return array_min(array_copy)
    if array_copy[1] > array_copy[0]:
        array_copy.remove(array_copy[1])
        return array_min(array_copy)


def test2(array_size):
    max_number = 100
    array = [random.randint(0, max_number) for _ in range(array_size)]

    num_min = array_min(array)
    num_max = array_max(array)

    index_min = array.index(num_min)
    index_max = array.index(num_max)
    array[index_min] = num_max
    array[index_max] = num_min
    # print (array)


#100 loops, best of 3: 76.1 usec per loop - 10
#100 loops, best of 3: 1.04 msec per loop - 100 в 13 раз
#100 loops, best of 3: 29.8 msec per loop - 1000 в 29 раз

#cProfile
#10/1    0.000    0.000    0.000    0.000 Task1_.py:46(array_max) -     10
#10/1    0.000    0.000    0.000    0.000 Task1_.py:57(array_min) -     10
#100/1    0.000    0.000    0.000    0.000 Task1_.py:46(array_max) -    100
#100/1    0.000    0.000    0.000    0.000 Task1_.py:57(array_min) -    100
#1    0.000    0.000    0.001    0.001 Task1_.py:68(test2) -            100
#1000/1    0.018    0.000    0.044    0.044 Task1_.py:46(array_max) -   1000
#1000/1    0.009    0.000    0.017    0.017 Task1_.py:57(array_min) -   1000
#1    0.000    0.000    0.067    0.067 Task1_.py:68(test2)              1000


#______________________________________________________________________________________________________________________

#Вариант3: с помощью max, min
def test3(array_size):
    max_number = 100
    array = [random.randint(0, max_number) for _ in range(array_size)]
    num_max = max(array)
    num_min = min(array)
    # print (item_min, item_max)
    index_min = array.index(num_min)
    index_max = array.index(num_max)
    array[index_min] = num_max
    array[index_max] = num_min
    # print (array)


#
# print(cProfile.run('test3(1000)'))

#100 loops, best of 3: 43.9 usec per loop -     10
#100 loops, best of 3: 399 usec per loop -      100
#100 loops, best of 3: 8.32 msec per loop -     1000
#100 loops, best of 3: 85.8 msec per loop -     10000

#cProfile
#1    0.000    0.000    0.000    0.000 Task1_.py:99(test3) -    10
#1    0.000    0.000    0.001    0.001 Task1_.py:99(test3) -    100
#1    0.000    0.000    0.006    0.006 Task1_.py:99(test3) -    1000

# python -m timeit -n 100 -s "import Task1_" "Task1_.test1(10)"

#______________________________________________________________________________________________________________________

# Вывод. Варианты 1 и 3 работают с очень похожей скоростью.
# Вариант 2  плохой. Глубина стека достигается при размерности массива в 1000. Скорость ниже в 4 раза, чем у
# двух других алгоритмов.


