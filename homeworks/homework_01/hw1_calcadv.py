#!/usr/bin/env python
# coding: utf-8

import re


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''

    if input_string == '':
        return None

    for c in input_string:
        if c not in ['0', '1', '2', '3', '4', '5', '6',
                     '7', '8', '9', '+', '-', '*', '/',
                     '(', ')', '.', ' ', '\t']:
            return None

    if re.search("^[^0-9]+$", input_string):
        return None

    if re.search("[\+\-\*/]$", input_string) or \
            re.search("^[\*/]", input_string):
        return None

    lst = re.findall(r"[\w+-/()*]+", input_string)

    for i in range(len(lst) - 1):
        try:
            float(lst[i])
            float(lst[i + 1])
            if float(lst[i + 1]) >= 0:
                return None
        except Exception:
            pass

    st = ''.join(lst)

    while True:
        st = st.replace('--', '+')
        st = st.replace('++', '+')
        st = st.replace('+-', '-')
        st = st.replace('-+', '-')

        cnt = 0
        cnt += (st.count('--') + st.count('++') +
                st.count('+-') + st.count('-+'))
        if cnt == 0:
            break

    if st[0] == '-':
        st_new = '0' + st
    else:
        st_new = st
    if st[0] == '+':
        st_new = st[1:]

    if re.search(r'\.[\d]+\.', st_new):
        return None

    if '()' in st_new or st_new.count('(') != st_new.count(')'):
        return None

    a, b = 0, 0
    for c in st_new:
        if c == '(':
            a += 1
        if c == ')':
            b += 1
        if a < b:
            return None

    while st_new.count('/-') != 0 or st_new.count('/+') != 0 \
            or st_new.count('*-') != 0 or st_new.count('*+') != 0:
        st_new = re.sub(r"([\d\+\-\(\)])([\/\*])([\-\+]\d+\.?[0-9]*)",
                        r"\1\2(0\3)", st_new)

    wrong = ['\+\*', '\+/', '\+\)', '\-\*', '-\/', '-\)', '\*\*', '\*/',
             '\*\)', '/\*', '//', '/\)', '\(\+', '\(-', '\(\*', '\(/',
             '\)\(', r'\)\d', r'\d\(', r'\.{2,}']
    for part in wrong:
        if re.search(part, st_new):
            return None

    priority = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
    st_new += '_'
    stek_numbers = []
    stek_oper = []
    stek_count = []
    num = ''

    for s in st_new:
        if s.isdigit() or s == '.':
            num += s
        elif num != '':
            stek_numbers.append(float(num))
            num = ''

        if s in ['+', '-', '*', '/'] \
                and (stek_oper == [] or priority[s] > priority[stek_oper[-1]]):
            stek_oper.append(s)
        elif s in ['+', '-', '*', '/'] \
                and priority[s] <= priority[stek_oper[-1]]:
            while stek_oper != [] and priority[s] <= priority[stek_oper[-1]]:
                stek_numbers.append(stek_oper.pop())
            stek_oper.append(s)
        elif s == '(':
            stek_oper.append(s)
        elif s == ')':
            while stek_oper[-1] != '(':
                stek_numbers.append(stek_oper.pop())
            stek_oper.pop()

    while stek_oper != []:
        stek_numbers.append(stek_oper.pop())

    for k in stek_numbers:
        if type(k) == float:
            stek_count.append(k)

        elif k == '+':
            stek_count.append(float(stek_count.pop()) +
                              float(stek_count.pop()))
        elif k == '-':
            stek_count.append(-float(stek_count.pop()) +
                              float(stek_count.pop()))
        elif k == '*':
            stek_count.append(float(stek_count.pop()) *
                              float(stek_count.pop()))
        elif k == '/':
            try:
                stek_count.append(1 / (float(stek_count.pop()) /
                                       float(stek_count.pop())))
            except ZeroDivisionError:
                return None

    return (stek_count[0])

    # raise NotImplementedError
