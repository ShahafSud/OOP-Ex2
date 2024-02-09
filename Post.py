from abc import ABC, abstractmethod


class Post(ABC):
    def __init__(self, owner):
        self._comments = []  # protected attribute
        self._likers = []  # protected attribute
        self._owner = owner  # protected attribute

    def like(self, User):
        self._likers.append(User)
        self._owner.addNotification(User.UN + "liked your post")

    def comment(self, User, string):
        self._comments.append(User)
        self._owner.addNotification(User.UN + "commented on your post: " + string)
