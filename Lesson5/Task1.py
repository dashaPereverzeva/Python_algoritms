__author__ = 'dashik'

#Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль
# ниже среднего.


from collections import namedtuple
from collections import defaultdict


Factory= namedtuple('Factory', 'name, quarter1, quarter2, quarter3, quarter4')
factories = {}
factories_number = 0
pribil_all = 0

while True:
    my_factory = Factory (input('Введите название предприятия '), int(input('Введите прибыль за 1 квартал ')),
                                                             int(input('Введите прибыль за 2 квартал ')),
                                                             int(input('Введите прибыль за 3 квартал ')),
                                                             int(input('Введите прибыль за 4 квартал ')))
    pribil = my_factory.quarter1 + my_factory.quarter2 + my_factory.quarter3 + my_factory.quarter4
    print (my_factory)
    factories[my_factory.name] = pribil
    pribil_all = pribil_all + pribil
    factories_number = factories_number +1
    respond = int(input('Ваш выбор \n'
                        '1. Ввести данные еще одного предприятия \n'
                        '2. Произвести расчет  \n'))
    if respond == 2:
        break
pribil_all = pribil_all / factories_number

list_below = []
list_above = []
for key, value in factories.items():
    if value > pribil_all:
        list_above.append(key)
    if value < pribil_all:
        list_below.append(key)
# print (factories)
# print (pribil_all)

print ('Прибыль выше средней у предприятий', end = ': ')
for i in list_above:
    print(i, end=', ')

print()
print ('Прибыль ниже средней у предприятий', end = ': ')
for i in list_below:
    print(i, end = ', ')
