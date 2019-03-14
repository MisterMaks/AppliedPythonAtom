#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        '''
        принимает на вход список отсортированных непоубыванию списков и число
        на выходе выдает один список длинной k, отсортированных по убыванию
        '''
        true_lst = []
        lst = []
        for small_list in list_of_lists:
            for number in small_list:
                lst.append((number, len(lst)))
        instance_maxheap = MaxHeap(lst)
        for i in range(k):
            true_lst.append(instance_maxheap.extract_maximum()[0])
        return true_lst
        # raise NotImplementedError
