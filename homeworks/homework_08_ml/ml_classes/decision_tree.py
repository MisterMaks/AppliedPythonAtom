#!/usr/bin/env python
# coding: utf-8

import numpy as np
from collections import Counter


class DecisionTreeClassifier:
    '''
    Пишем свой велосипед - дерево для классификации
    '''

    def __init__(self, max_depth=None, min_leaf_size=None, max_leaf_number=None, min_inform_criter=None):
        '''
        Инициализируем наше дерево
        :param max_depth: один из возможных критерием останова - максимальная глубина дерева
        :param min_leaf_size: один из возможных критериев останова - число элементов в листе
        :param max_leaf_number: один из возможных критериев останова - число листов в дереве.
        Нужно подумать как нам отобрать "лучшие" листы
        :param min_inform_criter: один из критериев останова - процент прироста информации, который
        считаем незначительным
        '''
        self.max_depth = max_depth
        self.min_leaf_size = min_leaf_size
        self.max_leaf_number = max_leaf_number
        self.min_inform_criter = min_inform_criter
        # Будем запоминать правильную последовательность отбора признаков
        self.seq_of_sig = []
        # Будем запоминать соответствующие пороги для признаков
        self.ths = []
        # Будем запоминать приросты информации
        self.Qs = []
        # Инициализируем глубину дерева
        self.depth = 0
        self.depth_left = 0
        self.depth_right = 0
        # Инициализируем число листов в дереве
        self.leaf = 1
        # Инициализируем метку
        self.mark = True
        # Список вероятностей
        self.p = []
        # raise NotImplementedError

    def compute_split_information(self, X, y, th):
        '''
        Вспомогательный метод, позволяющий посчитать джини/энтропию для заданного разбиения
        :param X: Матрица (num_objects, 1) - срез по какой-то 1 фиче, по которой считаем разбиение
        :param y: Матрица (num_object, 1) - целевые переменные
        :param th: Порог, который проверяется
        :return: прирост информации
        '''
        y_right = []
        y_left = []
        for i in range(len(y)):
            if X[i] > th:
                y_right.append(y[i, 0])
            else:
                y_left.append(y[i, 0])
        y = list(y[:, 0])
        counter_y = Counter(y)
        counter_y_left = Counter(y_left)
        counter_y_right = Counter(y_right)

        def H(counter):
            p = []
            for key, value in counter.items():
                p.append(value / sum(counter.values()))
            entropy = -sum(p * np.log2(p))
            return entropy

        Q = H(counter_y) - (len(y_left) / len(y) * H(counter_y_left) +
                            len(y_right) / len(y) * H(counter_y_right))
        return Q
        # raise NotImplementedError

    def fit(self, X, y, extra_param=None):
        '''
        Стендартный метод обучения
        :param X: матрица объекто-признаков (num_objects, num_features)
        :param y: матрица целевой переменной (num_objects, 1)
        :return: None
        '''

        th = X[0, 0]
        best_sign = 0
        Q = self.compute_split_information(X[:, 0], y, th)
        self.seq_of_sig.append(0)
        self.ths.append(th)
        self.Qs.append(Q)
        Xy = np.hstack((X, y))
        # i - строка, j - столбец
        for j in range(X.shape[1]):
            Xy = np.array(sorted(Xy, key=lambda x: x[j]))
            extra_X, extra_y = Xy[:, j], Xy[:, -1]
            for i in range(X.shape[0]):
                extra_th = extra_X[i]
                extra_Q = self.compute_split_information(extra_X, extra_y, extra_th)
                if extra_Q > Q:
                    best_sign = j
                    Q = extra_Q
                    th = extra_th
                    self.seq_of_sig.pop()
                    self.seq_of_sig.append(j)
                    self.ths.pop()
                    self.ths.append(th)
                    self.Qs.pop()
                    self.Qs.append(Q)
        self.leaf += 2
        # Условие на кол-во листов в дереве
        if self.leaf >= self.max_leaf_number:
            self.mark = False
            #return None
        # Условие на прирост информации
        if Q / self.Qs[-1] < self.min_inform_criter:
            self.mark = False
            #return None

        if extra_param is None:
            self.depth += 1
        if extra_param == "left":
            self.depth_left += 1
            if self.depth_left + 1 >= self.max_depth:
                self.mark = False
        if extra_param == "right":
            self.depth_right += 1
            if self.depth_right + 1 >= self.max_depth:
                self.mark = False

        y_left, y_right = [], []
        X_left, X_right = [], []
        for i in range(len(y)):
            if X[i, best_sign] > th:
                y_right.append(y[i, :])
                X_right.append(X[i, :])
            else:
                y_left.append(y[i, :])
                X_left.append(X[i, :])
        X_left = np.array(X_left)
        y_left = np.array(y_left)
        X_right = np.array(X_right)
        y_right = np.array(y_right)
        # Условие на число элементов в листе
        if len(y_left) >= self.min_leaf_size and self.mark is True:
            self.fit(X_left, y_left, extra_param="left")
        else:
            self.mark = False
        if len(y_right) >= self.min_leaf_size and self.mark is True:
            self.fit(X_right, y_right, extra_param="right")
        else:
            self.mark = False
        if self.mark is False:
            self.p = Counter(list())
        return None
        # raise NotImplementedError

    def predict(self, X):
        '''
        Метод для предсказания меток на объектах X
        :param X: матрица объектов-признаков (num_objects, num_features)
        :return: вектор предсказаний (num_objects, 1)
        '''

        raise NotImplementedError

    def predict_proba(self, X):
        '''
        метод, возвращающий предсказания принадлежности к классу
        :param X: матрица объектов-признаков (num_objects, num_features)
        :return: вектор предсказанных вероятностей (num_objects, 1)
        '''
        raise NotImplementedError
