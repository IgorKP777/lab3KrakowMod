from prettytable import PrettyTable
import indicative
import integral
import primitive
import rectangle
import trapezoid

n = 10000

table = PrettyTable()
table.title = 'Численное интегрирование'
table.field_names = ['Способ решения', 'Результат решения']
table.align = 'l'

integral_number = int
try:
    integral_number = int(input('введите номер интеграла '))
except ValueError:
    print('введите число')
    exit(-2)

i = float
if 1 <= integral_number <= 3:
    if integral_number == 1:
        table.add_row([primitive.primitive_1()[0], primitive.primitive_1()[1]])
        table.add_row([indicative.indicative_1()[0], indicative.indicative_1()[1]])
        table.add_row([trapezoid.trapezoid_1()[0], trapezoid.trapezoid_1()[1]])
        table.add_row([integral.integral_1()[0], integral.integral_1()[1]])
        table.add_row([rectangle.rectangle_1()[0], rectangle.rectangle_1()[1]])
        # graph_integral.graph_1()
    if integral_number == 2:
        table.add_row([primitive.primitive_2()[0], primitive.primitive_2()[1]])
        # table.add_row([indicative.indicative_2()[0], indicative.indicative_2()[1]])
        table.add_row([trapezoid.trapezoid_2()[0], trapezoid.trapezoid_2()[1]])
        table.add_row([integral.integral_2()[0], integral.integral_2()[1]])
        table.add_row([rectangle.rectangle_2()[0], rectangle.rectangle_2()[1]])
        # graph_integral.graph_2()
    if integral_number == 3:
        table.add_row([primitive.primitive_3()[0], primitive.primitive_3()[1]])
        # table.add_row([indicative.indicative_2()[0], indicative.indicative_2()[1]])
        table.add_row([trapezoid.trapezoid_3()[0], trapezoid.trapezoid_3()[1]])
        table.add_row([integral.integral_3()[0], integral.integral_3()[1]])
        table.add_row([rectangle.rectangle_3()[0], rectangle.rectangle_3()[1]])
        # graph_integral.graph_3()
    print(table)
else:
    print('введите номер интегралла от 1 до 3')
    exit(-3)
