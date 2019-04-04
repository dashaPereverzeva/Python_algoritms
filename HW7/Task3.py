__author__ = 'dashik'
import random

N = 21
li = [random.randint(0, 50) for _ in range(N)]
print (li)
print (sorted(li))
i = 0
j = 0
while i < len(li):
    count_l = 0
    count_r = 0
    while j < len(li):
        if i == j:
            # print("******")
            j = j + 1
            if j == len(li):
                break

        if li[i] == li[j]:
            if i > j:
                count_l = count_l + 1
            if i < j:
                count_r = count_r + 1
        if li[i] > li[j]:
            count_l = count_l + 1
        if li[i] < li[j]:
            count_r = count_r + 1
        j = j + 1
        # print (count_l, count_r)
    if count_l == count_r:
        med = li[i]
        break
    i = i + 1
    j = 0
    # print ('___________')

# проверка
li_sorted = sorted(li)

print ('Наш результат')
print (med)

print ('Вычисление после сортировки списка')

median = li_sorted[len(li_sorted) // 2]
print (median)
