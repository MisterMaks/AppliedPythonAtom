#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''

    if type(list_of_lists) != list:
        return None
    if len(list_of_lists) == 1:
        if type(list_of_lists[0]) != list:
            return list_of_lists[0]
        elif len(list_of_lists[0]) != 1:
            return None
        else:
            return list_of_lists[0][0]
    for i in list_of_lists:
        if type(i) == list:
            if len(i) != len(list_of_lists):
                return None
        else:
            return None

    def dopminor(matr, ind):
        minor = [[1] * len(matr) for i in range(len(matr))]
        for i in range(len(matr)):
            for j in range(len(matr)):
                minor[i][j] = matr[i][j]
        minor.pop(0)
        for i in range(len(minor)):
            minor[i].pop(ind)
        return minor

    res = 0
    if len(list_of_lists) <= 2:
        return list_of_lists[0][0] * list_of_lists[1][1] - \
               list_of_lists[0][1] * list_of_lists[1][0]
    else:
        for i in range(len(list_of_lists)):
            res += ((-1) ** (i)) * list_of_lists[0][i] * \
                   calculate_determinant(dopminor(list_of_lists, i))
    return res

    # raise NotImplementedError
