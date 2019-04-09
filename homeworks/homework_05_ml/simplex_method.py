#!/usr/bin/env python
# coding: utf-8

import numpy as np


def simplex_method(a, b, c):
    """
    Почитать про симплекс метод простым языком:
    * https://  https://ru.wikibooks.org/wiki/Симплекс-метод._Простое_объяснение
    Реализацию алгоритма взять тут:
    * https://youtu.be/gRgsT9BB5-8 (это ссылка на 1-ое из 5 видео).

    Используем numpy и, в целом, векторные операции.

    a * x.T <= b
    c * x.T -> max
    :param a: np.array, shape=(n, m)
    :param b: np.array, shape=(n, 1)
    :param c: np.array, shape=(1, m)
    :return x: np.array, shape=(1, m)
    """
    size_of_a = a.shape
    matrix = np.hstack((np.vstack((a, -c)),
                        np.eye(size_of_a[0] + 1),
                        np.vstack((b.reshape((size_of_a[0], 1)), 0))))
    while any(matrix[-1, :] < 0):
        true_col = matrix[-1, :].argmin()
        true_stroka = (matrix[:-1, -1] / matrix[:-1, true_col]).argmin()
        matrix[true_stroka, :] /= matrix[true_stroka, true_col]
        for stroka in range(size_of_a[0] + 1):
            if stroka != true_stroka:
                matrix[stroka, :] -= matrix[true_stroka, :] * matrix[stroka, true_col]
    x = np.zeros(size_of_a[1])
    for col in range(size_of_a[1]):
        if matrix[-1, col] == 0:
            x[col] = matrix[matrix[:, col].argmax(), -1]
    return x
    # raise NotImplementedError
