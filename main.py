import os
import sys

# Программа для подсчета средней арифметической и средней геометрической

x = list(input("Введите числа").split(' '))
list_of_int = []
for i in x:
    list_of_int.append(int(i))


def helps():
    print("Используйте -aA для вычесления средней арифметической")
    print("Используйте -aG для вычесления средней арифметической")
    print("Используйте -help для вызова справки")


def arithmetic():
    average_arithm = sum(list_of_int) / len(list_of_int)
    return average_arithm


def geometric():
    multi = 1
    for i in list_of_int:
        multi *= i
    average_geom = multi ** (1 / len(list_of_int))
    return average_geom

