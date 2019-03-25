#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager, Pool, Queue
import os


def word_count_inference(path_to_dir):
    '''
    Метод, считающий количество слов в каждом файле из директории
    и суммарное количество слов.
    Слово - все, что угодно через пробел, пустая строка "" словом не считается,
    пробельный символ " " словом не считается. Все остальное считается.
    Решение должно быть многопроцессным. Общение через очереди.
    :param path_to_dir: путь до директории с файлами
    :return: словарь, где ключ - имя файла, значение - число слов +
        специальный ключ "total" для суммы слов во всех файлах
    '''
    result_dict = {}
    total_count_words = 0
    queue = Queue()
    for filename in os.listdir(path_to_dir):
        queue.put(filename)
    with Pool(3) as p:
        while not queue.empty():
            filename = queue.get()
            path_to_file = path_to_dir + "/" + filename
            count_words = p.apply(count_word_in_file, (path_to_file,))
            result_dict[filename] = count_words
            total_count_words += count_words
    result_dict["total"] = total_count_words
    return result_dict
    # raise NotImplementedError


def count_word_in_file(filename):
    count_words = 0
    with open(filename, "r") as f:
        for line in f:
            count_words += len(line.split())
    return count_words
