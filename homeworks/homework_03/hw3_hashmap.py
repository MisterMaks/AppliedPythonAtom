#!/usr/bin/env python
# coding: utf-8


class HashMap:
    '''
    Давайте сделаем все объектненько,
     поэтому внутри хешмапы у нас будет Entry
    '''

    class Entry:
        def __init__(self, key, value):
            '''
            Сущность, которая хранит пары ключ-значение
            :param key: ключ
            :param value: значение
            '''
            self.key = key
            self.value = value

        def get_key(self):
            # TODO возвращаем ключ
            return self.key
            # raise NotImplementedError

        def get_value(self):
            # TODO возвращаем значение
            return self.value
            # raise NotImplementedError

        def __eq__(self, other):
            # TODO реализовать функцию сравнения
            return self.key == other.key
            # raise NotImplementedError

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self.buckets = [[] for _ in range(bucket_num)]
        self.size = bucket_num
        self.count = 0
        # raise NotImplementedError

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        hash_key = self._get_hash(key)
        index = self._get_index(hash_key)
        for element in self.buckets[index]:
            if element.get_key() == key:
                return element.get_value()
        return default_value
        # raise NotImplementedError

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        hash_key = self._get_hash(key)
        index = self._get_index(hash_key)
        for element in self.buckets[index]:
            if element.get_key() == key:
                element.value = value
                return None
        self.buckets[index].append(self.Entry(key, value))
        self.count += 1
        if self.count >= (2 / 3) * self.size:
            self._resize()
        return None
        # raise NotImplementedError

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self.count
        # raise NotImplementedError

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)
        # raise NotImplementedError

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % self.size
        # raise NotImplementedError

    def values(self):
        # TODO Должен возвращать итератор значений
        return ValuesIterator(self)
        # raise NotImplementedError

    def keys(self):
        # TODO Должен возвращать итератор ключей
        return KeysIterator(self)
        # raise NotImplementedError

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        return ItemsIterator(self)
        # raise NotImplementedError

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        items = [(key, value) for key, value in self.items()]
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0
        for element in items:
            self.put(element[0], element[1])
        # raise NotImplementedError

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        return "buckets: {}, items: {}".format(self.buckets, self.items())
        # raise NotImplementedError

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        hash_item = self._get_hash(item)
        index = self._get_index(hash_item)
        for element in self.buckets[index]:
            if element.get_key() == item:
                return True
        return False
        # raise NotImplementedError


class ValuesIterator:
    def __init__(self, hashmap):
        self.hashmap = hashmap
        self.counter = 0
        self.extra_counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter < self.hashmap.size:
            while self.extra_counter < len(self.hashmap.buckets[self.counter]):
                self.extra_counter += 1
                return self.hashmap.buckets[self.counter][self.extra_counter - 1].get_value()
            self.counter += 1
            self.extra_counter = 0
        raise StopIteration


class KeysIterator:
    def __init__(self, hashmap):
        self.hashmap = hashmap
        self.counter = 0
        self.extra_counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter < self.hashmap.size:
            while self.extra_counter < len(self.hashmap.buckets[self.counter]):
                self.extra_counter += 1
                return self.hashmap.buckets[self.counter][self.extra_counter - 1].get_key()
            self.counter += 1
            self.extra_counter = 0
        raise StopIteration


class ItemsIterator:
    def __init__(self, hashmap):
        self.hashmap = hashmap
        self.counter = 0
        self.extra_counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter < self.hashmap.size:
            while self.extra_counter < len(self.hashmap.buckets[self.counter]):
                self.extra_counter += 1
                return (self.hashmap.buckets[self.counter][self.extra_counter - 1].get_key(),
                        self.hashmap.buckets[self.counter][self.extra_counter - 1].get_value())
            self.counter += 1
            self.extra_counter = 0
        raise StopIteration
