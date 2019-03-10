#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:
    def __init__(self):
        self.users = {}
        self.posts = {}
        # raise NotImplementedError

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id in self.users:
            self.users[user_id]["post_id"].append(post_id)
        else:
            self.users[user_id] = {"post_id": [post_id],
                                   "followee_user_id": []}
        self.posts[post_id] = {"user_id": [], "read": 0}
        # pass

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id in self.posts:
            if user_id not in self.posts[post_id]["user_id"]:
                self.posts[post_id]["user_id"].append(user_id)
                self.posts[post_id]["read"] += 1
        else:
            self.posts[post_id] = {"user_id": [user_id], "read": 1}
            # pass

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id in self.users:
            self.users[follower_user_id]["followee_user_id"] \
                .append(followee_user_id)
        else:
            self.users[follower_user_id] = \
                {"followee_user_id": [followee_user_id], "post_id": []}
            # pass

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        recent_posts = []
        for followee in self.users[user_id]["followee_user_id"]:
            recent_posts += self.users[followee]["post_id"]
        return sorted(recent_posts, reverse=True)[:k]
        # pass

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        popular_posts = []
        sort_pop_posts = sorted(self.posts.items(), key=lambda x: x[1]["read"],
                                reverse=True)
        sort_rec_posts = sorted(sort_pop_posts, reverse=True)
        new_sort_pop_posts = sorted(sort_rec_posts, key=lambda x: x[1]["read"],
                                    reverse=True)[:k]
        for post in range(len(new_sort_pop_posts)):
            popular_posts.append(new_sort_pop_posts[post][0])
        return popular_posts
        # pass
