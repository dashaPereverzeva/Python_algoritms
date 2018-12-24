__author__ = 'dashik'
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.

A = [555, 666, 777, 888, 67676]
otvet_sum = 0
otvet = 0
for i in A:
    backup_i = i
    result = 0
    while i > 0:
        result = result + i%10
        i=i//10
    if result > otvet_sum:
        otvet_sum = result
        otvet = backup_i
print (otvet, otvet_sum)
