#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.dict_users = {}
        # raise NotImplementedError

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        if self.dict_users.get(user_id):
            if self.dict_users[user_id].get(time):
                self.dict_users[user_id][time] += 1
            else:
                self.dict_users[user_id][time] = 1
        else:
            self.dict_users[user_id] = {time: 1}
        return None
        # raise NotImplementedError

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        # TODO: реализовать метод
        activity_count = 0
        if count == 0:
            return activity_count
        for user_key in self.dict_users.keys():
            count_event_of_user = 0
            for time_key in self.dict_users[user_key].keys():
                if time_key > time - self.FIVE_MIN and time_key <= time:
                    count_event_of_user += self.dict_users[user_key][time_key]
            if count_event_of_user == count:
                activity_count += 1
        return activity_count
        # raise NotImplementedError
