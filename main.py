from prettytable import PrettyTable

import graph_integral
import integral
import art

integral_number = int
try:
    integral_number = int(input('введите номер интеграла '))
except ValueError:
    print('введите число')
    exit(-2)

table = PrettyTable()
table.title = 'Результаты'
table.field_names = ['Способ решения', '123']
print(table)

intgrl = integral
i = float
if 1 <= integral_number <= 3:
    if integral_number == 1:
        i = intgrl.integral_1()
        print(art.text2art('I = ' + str(round(number=i, ndigits=4)), 'block'))
        graph_integral.graph_1()
    if integral_number == 2:
        i = intgrl.integral_2()
        print(art.text2art('I = ' + str(round(number=i, ndigits=4)), 'block'))
        graph_integral.graph_2()
    if integral_number == 3:
        i = intgrl.integral_3()
        print(art.text2art('I = ' + str(round(number=i, ndigits=4)), 'block'))
        graph_integral.graph_3()
else:
    print('введите номер интегралла от 1 до 3')
