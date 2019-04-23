#!/usr/bin/env python
# coding: utf-8


import numpy as np


def logloss(y_true, y_pred):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    return - np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    # pass


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    TP_TN = 0
    for i in range(y_pred.size):
        if y_pred[i] == y_true[i]:
            TP_TN += 1
    return TP_TN / y_pred.size
    # pass


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    TP = 0
    TP_FP = 0
    for i in range(y_pred.size):
        if y_pred[i] == y_true[i] and y_pred[i] == 1:
            TP += 1
        if y_pred[i] == 1:
            TP_FP += 1
    return TP / TP_FP
    # pass


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    TP = 0
    TP_FN = 0
    for i in range(y_pred.size):
        if y_pred[i] == y_true[i] and y_pred[i] == 1:
            TP += 1
        if y_true[i] == 1:
            TP_FN += 1
    return TP / TP_FN
    # pass


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    TPR_list = []
    FPR_list = []
    y_class_list = []
    porogs = np.linspace(1, 0, 101)
    for porog in porogs:
        for i in range(y_pred.size):
            if y_pred[i] >= porog:
                y_class_list.append(1)
            else:
                y_class_list.append(0)
        TPR_list.append(recall(y_true, np.array(y_class_list)))
        FPR_list.append(fpr(y_true, np.array(y_class_list)))
        y_class_list = []
    return np.trapz(TPR_list, FPR_list)
    # pass


def fpr(y_true, y_pred):
    FP = 0
    FP_TN = 0
    for i in range(y_pred.size):
        if y_pred[i] != y_true[i] and y_pred[i] == 1:
            FP += 1
        if y_true[i] == 0:
            FP_TN += 1
    return FP / FP_TN
