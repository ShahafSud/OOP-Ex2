from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


class User:
    def __init__(self, UserName, Password):
        self.UN = UserName
        self.__PW = Password
        self.__loggedIn = True
        self.__followers = {}
        self.__following = {}
        self.__posts = []
        self.__notifications = []

    def validat_pass(self,PW):
        return self.__PW==PW
    # addfollower to targer and following to self
    def follow(self, followed):
        if self.__loggedIn==False or followed==self:
            return
        print(self.UN + " started following " + followed.UN)
        self.__following[followed.UN]=followed
        followed.__followers[self.UN]=self
    def unfollow(self, unfollowed):
        if self.__loggedIn == False or not unfollowed not in self.__following:
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
        if self.__loggedIn==False:
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
        for folower in self.__followers.values():
            folower.__notifications.append(self.UN + " has a new post")
    def __str__(self):
        return f"User name: {self.UN}, Number of posts: {len(self.__posts)},Number of followers: {len(self.__followers)}"
