from prettytable import PrettyTable
import graph_integral
import indicative
import integral
import art
import primitive
import trapezoid

table = PrettyTable()
table.title = 'Численное интегрирование'
table.field_names = ['Способ решения', 'Результат решения']

integral_number = int
try:
    integral_number = int(input('введите номер интеграла '))
except ValueError:
    print('введите число')
    exit(-2)

intgrl = integral
i = float
if 1 <= integral_number <= 3:
    if integral_number == 1:
        i = intgrl.integral_1()
        # print(art.text2art(text='I = ' + str(round(number=i, ndigits=4)), font='block'))
        table.add_row([primitive.primitive_1()[0], primitive.primitive_1()[1]])
        table.add_row([indicative.indicative_1()[0], indicative.indicative_1()[1]])
        table.add_row([trapezoid.trapezoid_1()[0], trapezoid.trapezoid_1()[1]])
        table.add_row(['Метод Монте-Карло', round(number=i, ndigits=4)])
        # graph_integral.graph_1()
    if integral_number == 2:
        i = intgrl.integral_2()
        # print(art.text2art('I = ' + str(round(number=i, ndigits=4)), 'block'))
        print('I = ' + str(round(number=i, ndigits=4)))
        graph_integral.graph_2()
    if integral_number == 3:
        i = intgrl.integral_3()
        # print(art.text2art('I = ' + str(round(number=i, ndigits=4)), 'block'))
        print('I = ' + str(round(number=i, ndigits=4)))
        graph_integral.graph_3()
    print(table)
else:
    print('введите номер интегралла от 1 до 3')
