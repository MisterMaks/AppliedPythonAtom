#!/usr/bin/env python
# coding: utf-8

import numpy as np
from sklearn.metrics import mean_squared_error


class DecisionStumpRegressor:
    '''
    Класс, реализующий решающий пень (дерево глубиной 1)
    для регрессии. Ошибку считаем в смысле MSE
    '''

    def __init__(self):
        '''
        Мы должны создать поля, чтобы сохранять наш порог th и ответы для
        x <= th и x > th
        '''
        self.th = 0
        self.y1 = None
        self.y2 = None
        # raise NotImplementedError

    def fit(self, X, y):
        '''
        метод, на котором мы должны подбирать коэффициенты th, y1, y2
        :param X: массив размера (1, num_objects)
        :param y: целевая переменная (1, num_objects)
        :return: None
        '''
        mse = mean_squared_error(y, 0)
        extra_y = np.zeros(y.shape)
        Xy = np.array(sorted(zip(X, y)))
        X, y = Xy[:, 0], Xy[:, 1]
        for i in range(len(X) - 1):
            th = np.mean(X[i:i + 2])
            left = np.mean(y[:i + 1])
            right = np.mean(y[i + 1:])
            extra_y[:i + 1] = left
            extra_y[i + 1:] = right
            if mse > mean_squared_error(y, extra_y):
                self.th = th
                self.y1 = left
                self.y2 = right
                mse = mean_squared_error(y, extra_y)
        return None
        # raise NotImplementedError

    def predict(self, X):
        '''
        метод, который позволяет делать предсказания для новых объектов
        :param X: массив размера (1, num_objects)
        :return: массив, размера (1, num_objects)
        '''
        y = []
        for i in range(len(X)):
            if X[i] >= self.th:
                y.append(self.y1)
            else:
                y.append(self.y2)
        return np.array(y)
        # raise NotImplementedError
