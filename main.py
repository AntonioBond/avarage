import sys
from newList import NewList

# Программа для подсчета средней арифметической и средней геометрической


def helps():
    print("Используйте -aA для вычесления средней арифметической")
    print("Используйте -aG для вычесления средней арифметической")
    print("Используйте -help для вызова справки")




try:
    numeric_list = sys.argv[2:]
    list_of_int = NewList([])
    for i in numeric_list:
        list_of_int.append(int(i))
except IndexError:
    list_of_int = []
do = {
    '-help': helps,
    '-aA': list_of_int.arithmetic,
    '-aG': list_of_int.geometric
}

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