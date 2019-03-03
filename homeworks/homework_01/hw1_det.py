#!/usr/bin/env python
# coding: utf-8

import numpy as np


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''

    try:
        return np.linalg.det(list_of_lists)
    except Exception:
        return None

    # raise NotImplementedError
