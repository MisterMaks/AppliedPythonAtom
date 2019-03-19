#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        # TODO Сделать правильно =)
        super().__init__()
        # raise NotImplementedError

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        return super().__contains__(key)
        # raise NotImplementedError

    def put(self, key, value=None):
        # TODO метод put, нужно переопределить данный метод
        super().put(key, value)
        # raise NotImplementedError

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return super().__len__()
        # raise NotImplementedError

    def values(self):
        # TODO возвращать итератор значений
        return super().keys()
        # raise NotImplementedError

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        keys = [key for key in self.keys()]
        another_keys = [key for key in another_hashset.keys()]
        new_hashset = HashSet()
        for key in keys:
            if key in another_keys:
                new_hashset.put(key)
        return new_hashset
        # raise NotImplementedError
