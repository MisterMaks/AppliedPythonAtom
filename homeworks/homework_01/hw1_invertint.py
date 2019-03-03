#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''

    n = str(number)
    sp = []
    for i in n:
        sp.append(i)
    if sp[0] == "-":
        sp.pop(0)
        sp.reverse()
        n = "".join(sp)
        n = -int(n)
        return n
    else:
        sp.reverse()
    n = "".join(sp)
    n = int(n)
    return n

    # raise NotImplementedError
