import sys

# Программа для подсчета средней арифметической и средней геометрической


def helps():
    print("Используйте -aA для вычесления средней арифметической")
    print("Используйте -aG для вычесления средней арифметической")
    print("Используйте -help для вызова справки")


def arithmetic():
    average_arithm = sum(list_of_int) / len(list_of_int)
    print(average_arithm)


def geometric():
    multi = 1
    for i in list_of_int:
        multi *= i
    average_geom = multi ** (1 / len(list_of_int))
    print(average_geom)

do = {
    '-help': helps,
    '-aA': arithmetic,
    '-aG': geometric
}


try:
    numeric_list = sys.argv[2:]
    list_of_int = []
    for i in numeric_list:
        list_of_int.append(int(i))
except IndexError:
    list_of_int = []


try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if key in do:
        do[key]()
    else:
        print('задан неверный ключ')
else:
    print("Ключ не задан")