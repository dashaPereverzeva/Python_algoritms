__author__ = 'dashik'
# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

A = int(input('Введите натуральное число '))

even_numb = 0
odd_numb = 0
while A > 0:
    i = A % 10
    A = A//10
    if i%2 == 0:
        even_numb = even_numb +1
    else:
        odd_numb = odd_numb+1

print ('Количество четных цифр: ', even_numb, 'Количество нечетных цифр: ',odd_numb)




