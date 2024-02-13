from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost

# A User is a factory of posts
class User:
    def __init__(self, UserName, Password):
        self.UN = UserName
        self.__PW = Password
        self.__loggedIn = True
        self.__followers = {} # User is an Observer on posts, a post will notify all its owners followers
        self.__following = {} # for unfollow
        self.__posts = []
        self.__notifications = []

    def validate_pass(self, PW):
        return self.__PW == PW
    # add follower to target and following to self
    def follow(self, followed):
        if not self.__loggedIn or followed == self:
            return
        print(self.UN + " started following " + followed.UN)
        self.__following[followed.UN]=followed
        followed.__followers[self.UN]=self
    def unfollow(self, unfollowed):
        if not self.__loggedIn or not unfollowed not in self.__following:
            return
        print(self.UN + " unfollowed " + unfollowed.UN)
        del self.__following[unfollowed.UN]
        del unfollowed.__followers[self.UN]
    # log in and out
    def login(self, PW):
        if PW != self.__PW or self.__loggedIn:
            return
        self.__loggedIn = True
        print(self.UN + " connected")
    def logout(self):
        if not self.__loggedIn:
            return
        self.__loggedIn = False
        print(self.UN + " disconnected")
    def publish_post(self, type, text_input, price=None, location=None):
        # Using the strategies design pattern to construct diffrent posts.
        if not self.__loggedIn:
            return
        if type == "Image":
            post = ImagePost(self, text_input)
            self.__posts.append(post)
            return post
        if type == "Text":
            post = TextPost(self, text_input)
            self.__posts.append(post)
            return post
        if type == "Sale":
            post = SalePost(self, text_input, price, location)
            self.__posts.append(post)
            return post
    # add notification to self
    def addNotification(self, string1, string2):
        self.__notifications.append(string1)
        print("notification to " + self.UN + ": " + string1 + string2)
    def print_notifications(self):
        print(self.UN + "'s notifications:")
        for notific in self.__notifications:
            print(notific)

    def send_post_notifications(self):
        for follower in self.__followers.values():
            follower.__notifications.append(self.UN + " has a new post")
    def __str__(self):
        return f"User name: {self.UN}, Number of posts: {len(self.__posts)},Number of followers: {len(self.__followers)}"
