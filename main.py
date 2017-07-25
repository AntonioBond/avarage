# Программа для подсчета средней арифметической и средней геометрической

x = list(input("Введите числа").split(' '))
list_of_int = []
for i in x:
    list_of_int.append(int(i))


averageArifm = sum(list_of_int) / len(list_of_int)
print(averageArifm)

multi = 1
for i in list_of_int:
    multi *= i

averageGeom = multi ** (1 / len(list_of_int))
print(averageGeom)
