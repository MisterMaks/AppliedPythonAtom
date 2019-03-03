#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''

    s = []
    for i in input_string:
        s.append(i)
        for j in range(1, len(s)):
            if s[j] == ")" and s[j - 1] == "(" \
                    or s[j] == "]" and s[j - 1] == "[" \
                    or s[j] == "}" and s[j - 1] == "{":
                del s[j]
                del s[j - 1]
    if len(s) == 0:
        return True
    else:
        return False

    # raise NotImplementedError
