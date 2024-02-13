from abc import ABC, abstractmethod

# This class implements 3 strategies, for each, an inheriting class have been created.

class Post(ABC):
    def __init__(self, owner):
        self._comments = []  # protected attribute
        self._likers = []  # protected attribute
        self._owner = owner  # protected attribute
        self._owner.send_post_notifications() # When created notify all observing users (followers of the owner)

    def like(self, User):
        if User.UN == self._owner.UN:
            return
        self._likers.append(User)
        self._owner.addNotification(User.UN + " liked your post", "")# When Liked notify all observing users (followers of the owner)

    def comment(self, User, string):
        if User.UN == self._owner.UN:
            return
        self._comments.append(User)
        self._owner.addNotification(User.UN + " commented on your post", ": " + string)# When commented notify all observing users (followers of the owner)
