__author__ = 'dashik'
import cProfile
import math

# Вариант 1 c решетом: размерность массива циклически увеличивается на 100
def list_prime(array_length):
    array = [0] * (array_length + 1)
    for i in range(array_length + 1):
        array[i] = i
    array[1] = 0
    for i in array:
        j = 2
        if i != 0:
            while i * j <= array_length:
                array[(i * j)] = 0
                j = j + 1
    list_of_primes = []
    for i in array:
        if i != 0:
            list_of_primes.append(i)
    return (list_of_primes)


def index_prime_num2(numb):
    n = 100
    while True:
        result = list_prime(n)
        if numb <= len(result) - 1:
            prime_num = result[numb - 1]
            return (prime_num)
        else:
            n = 2 * n

## print(index_prime_num2(110))
#100 loops, best of 3: 3.28 msec per loop - 100
#100 loops, best of 3: 80.8 msec per loop - 1000 в 26 раз
#10 loops, best of 3: 1.56 sec per loop - 10000 в 19 раз
#2 loops, best of 3: 13.6 sec per loop - 100000 в 13 раз
#2 loops, best of 3: 115 sec per loop - 500000 в 10 раз

# cProfile
# 1    0.000    0.000    0.002    0.002 Task2.py:23(index_prime_num2) - 100
# 4    0.002    0.000    0.002    0.001 Task2.py:59(list_prime)
# 1    0.000    0.000    0.101    0.101 Task2.py:23(index_prime_num2) - 1000
# 8    0.042    0.005    0.042    0.005 Task2.py:61(list_prime)
# 1    0.004    0.004    1.648    1.648 Task2.py:23(index_prime_num2) - 10000
# 12    1.617    0.135    1.652    0.138 Task2.py:62(list_prime)

#_____________________________________________________________________________________________________________________

# Вариант 2 с решетом: размерность массива заранее высчиывается по формуле k = n/ln(n)
def dimension(numb):
    length = 100
    quantity = 0
    array_size = []
    while quantity < numb:
        quantity  = length // math.log1p(length)
        array_size = [length, quantity]
        length = length + 100
    return (array_size[0])


def list_prime(array_length):
    array = [0] * (array_length + 1)
    for i in range(array_length + 1):
        array[i] = i
    array[1] = 0
    for i in array:
        j = 2
        if i != 0:
            while i * j <= array_length:
                array[(i * j)] = 0
                j = j + 1
    list_of_primes = []
    for i in array:
        if i != 0:
            list_of_primes.append(i)
    return (list_of_primes)

def index_prime_num1(numb):
    array_length = dimension(numb)
    while True:
        b = list_prime(array_length)
        if numb <= len(b) - 1:
            prime_num = b[numb - 1]
            return (prime_num)

# print(index_prime_num1(numb))

# index_prime_num1(10000)

#100 loops, best of 3: 1.15 msec per loop - 100
#100 loops, best of 3: 29.6 msec per loop - 1000 ---- в 30 раз
#10 loops, best of 3: 434 msec per loop - 10000  ---- в 14 раз
#2 loops, best of 3: 5.99 sec per loop - 100000  ---- в 14 раз
#2 loops, best of 3: 35.9 sec per loop - 500000  ---- в 6 раз

#cProfile
# 1    0.000    0.000    0.001    0.001 Task2.py:76(index_prime_num1) -100
# 1    0.000    0.000    0.000    0.000 Task2.py:48(dimension)
# 1    0.001    0.001    0.001    0.001 Task2.py:59(list_prime)
# 1    0.000    0.000    0.017    0.017 Task2.py:76(index_prime_num1) - 1000
# 1    0.000    0.000    0.000    0.000 Task2.py:48(dimension)
# 1    0.001    0.001    0.444    0.444 Task2.py:76(index_prime_num1) - 10000
# 1    0.002    0.002    0.002    0.002 Task2.py:48(dimension)
# 1    0.439    0.439    0.441    0.441 Task2.py:59(list_prime)
#_____________________________________________________________________________________________________________________

# Вариант 3: Без решета
def index_prime_num3(numb):
    result=[2]
    i = 3
    while len(result) < numb:
        delitel = 2
        prime = i
        while delitel < i:
            if i % delitel == 0:
                prime = 0
                break
            delitel = delitel +1
        if prime != 0:
            result.append(prime)
        i=i+1
    return result[numb-1]

# print(index_prime_num3(100))

#100 loops, best of 3: 71 usec per loop - 10
#100 loops, best of 3: 10.9 msec per loop - 100 в 153 раза
#100 loops, best of 3: 3.89 sec per loop - 1000 в 353 раза
#1 loops, best of 1: 530 sec per loop - 10000 в 132 раза

#cProfile
# 1    0.011    0.011    0.011    0.011 Task2.py:42(index_prime_num3) 100
#1    3.923    3.923    3.937    3.937 Task2.py:42(index_prime_num3) - 1000

print(cProfile.run('index_prime_num2(10000)'))

# Вывод. Оптимальным алгоритмлм является алгоритс с решетом и заранее подобранным размером массива (вариант 2).
# Разрыв вскорости между вариантами 1 и 2
# увеличивается по мере увеличения размера массива. Если при значении i (порядковый номер простого числа) 1000 и 10000
# скорость варианта 2 выше скорости варианта 3 приблизительно в 2 раза, то при более высоких значениях - в 5 раз.
#  Вариант 3 имеет квадратичную сложность, работает в 1000 раз много раз медленнее, если я все правильно поняла.
#
