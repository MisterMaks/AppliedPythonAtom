#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''

    if type(source_dict) is str:
        return source_dict

    d = {}
    for key, value in source_dict.items():
        if type(value) in [list, tuple, set]:
            value = list(value)
            i = 0
            while i != len(value):
                if type(value[i]) in [list, tuple, set]:
                    value[i] = list(value[i])
                    sublist = value[i]
                    value.pop(i)
                    for j in range(len(sublist)):
                        value.insert(i + j, sublist[j])
                    continue
                i += 1
            for ind in value:
                if d.get(ind) is None:
                    d[ind] = key
                else:
                    if type(d[ind]) is not list:
                        d[ind] = [d[ind]]
                    d[ind].append(key)
        else:
            if d.get(value) is None:
                d[value] = key
            else:
                if type(d[value]) is not list:
                    d[value] = [d[value]]
                d[value].append(key)
    return d

    # raise NotImplementedError
