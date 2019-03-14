#!/usr/bin/env python
# coding: utf-8


class Heap():
    def __init__(self, array):
        self.array = array[:]
        self.build_heap()
        # pass

    def add(self, elem_with_priority):
        self.array.append(elem_with_priority)
        self.sift_up()
        # pass

    def build_heap(self):
        for i in range(len(self.array) // 2 - 1, -1, -1):
            self.sift_down(i)
            # pass

    def sift_up(self):
        index = len(self.array) - 1
        while index > 0:
            parent = (index - 1) // 2
            if comparator_d(self.array[parent], self.array[index]):
                return True
            self.array[index], self.array[parent] = \
                self.array[parent], self.array[index]
            index = parent

    def sift_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < len(self.array) and \
                comparator_d(self.array[left], self.array[i]):
            largest = left
        if right < len(self.array) and \
                comparator_d(self.array[right], self.array[largest]):
            largest = right
        if largest != i:
            self.array[i], self.array[largest] = \
                self.array[largest], self.array[i]
            self.sift_down(largest)


class MaxHeap(Heap):
    def __init__(self, array):
        super().__init__(array)
        # raise NotImplementedError

    def extract_maximum(self):
        maximum = 0
        if len(self.array) > 0:
            maximum = self.array.pop(0)
            if len(self.array) > 0:
                self.array.insert(0, self.array.pop())
                self.sift_down(0)
        return maximum
        # pass


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
