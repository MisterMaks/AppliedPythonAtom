#!/usr/bin/env python
# coding: utf-8


import numpy as np
import copy


class LogisticRegression:
    def __init__(self, lambda_coef=1.0, regulatization=None, alpha=0.5, n_iter=100):
        """
        LogReg for Binary case
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.lambda_coef = lambda_coef
        self.regulatization = regulatization
        self.alpha = alpha
        self.n_iter = n_iter
        # pass

    def fit(self, X_train, y_train, eps=0.005):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        assert X_train.shape[0] == y_train.shape[0], \
            "Размеры X_train и y_train не совпадают! Не надо так!!!"
        self.status = True
        self.weights = np.random.randn(X_train.shape[1] + 1)
        extra_weights = self.weights
        n = X_train.shape[0]
        X = np.hstack([np.ones((n, 1)), X_train])
        if self.regulatization is None:
            for i in range(self.n_iter):
                sigma = 1 / (1 + np.exp(-np.dot(X, self.weights)))
                grad_Q = np.dot(X.T, (sigma - y_train)) / n
                if abs(extra_weights - (self.weights - self.lambda_coef * grad_Q)).all() <= eps:
                    break
                self.weights -= self.lambda_coef * grad_Q
                extra_weights = self.weights
        if self.regulatization == "L1":
            for i in range(self.n_iter):
                sigma = 1 / (1 + np.exp(-np.dot(X, self.weights)))
                grad_Q = np.dot(X.T, (sigma - y_train)) / n + self.alpha * np.sign(self.weights) / n
                if abs(extra_weights - (self.weights - self.lambda_coef * grad_Q)).all() <= eps:
                    break
                self.weights -= self.lambda_coef * grad_Q
                extra_weights = self.weights
        if self.regulatization == "L2":
            for i in range(self.n_iter):
                sigma = 1 / (1 + np.exp(-np.dot(X, self.weights)))
                grad_Q = np.dot(X.T, (sigma - y_train)) / n + 2 * self.alpha * self.weights / n
                if abs(extra_weights - (self.weights - self.lambda_coef * grad_Q)).all() <= eps:
                    break
                self.weights -= self.lambda_coef * grad_Q
                extra_weights = self.weights
        return None
        # pass

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        assert self.status is True, \
            "Модель не обучена! Не надо так!!!"
        result = np.vectorize(lambda x: round(x))
        return result(self.predict_proba(X_test))
        # pass

    def predict_proba(self, X_test):
        """
        Predict probability using model.
        :param X_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        assert self.status is True, \
            "Модель не обучена! Не надо так!!!"
        X_test = np.hstack([np.ones((X_test.shape[0], 1)), X_test])
        sigma = 1 / (1 + np.exp(-np.dot(X_test, self.weights)))
        return np.column_stack([1 - sigma, sigma])
        # pass

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        assert self.status is True, \
            "Модель не обучена! Не надо так!!!"
        return self.weights
        # pass
