#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    '''
    Метод возвращает индексы двух различных
    элементов listа, таких, что сумма этих элементов равна
    n. В случае, если таких элементов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    '''

    mnoj = {}
    for i, el in enumerate(input_list):
        dop = n - el
        if dop in mnoj:
            return mnoj[dop], i
        elif el != n - el:
            mnoj[el] = i
    return None

    # raise NotImplementedError
