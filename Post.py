from abc import ABC, abstractmethod


class Post(ABC):
    def __init__(self, owner):
        self._comments = []  # protected attribute
        self._likers = []  # protected attribute
        self._owner = owner  # protected attribute
        self._owner.send_post_notifications()

    def like(self, User):
        if User.UN == self._owner.UN:
            return
        self._likers.append(User)
        self._owner.addNotification(User.UN + " liked your post", "")

    def comment(self, User, string):
        if User.UN == self._owner.UN:
            return
        self._comments.append(User)
        self._owner.addNotification(User.UN + " commented on your post", ": " + string)
