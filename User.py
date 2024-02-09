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
        if self.__loggedIn==False:
            return
        print(self.UN + "started following" + followed.UN)
        self.__following[followed.UN]=followed
        followed.__followers[self.UN]=self
    def unfollow(self, unfollowed):
        if self.__loggedIn==False:
            return
        print(self.UN + "unfollowed" + unfollowed.UN)
        del self.__following[unfollowed.UN]
        del unfollowed.__followers[self.UN]
    # log in and out
    def login(self):
        self.__loggedIn=True
    def logout(self):
        self.__loggedIn=False
    #support all three post types
    def publish_post(self, type, textOrPath):
        if self.__loggedIn==False:
            return
        if type == "Image":
            return ImagePost(textOrPath)
        if type == "Text":
            return TextPost(textOrPath)
    def publish_post(self, type, discription, price, location):
        if self.__loggedIn==False:
            return
        if type == "Sale":
            return SalePost(discription, price, location)
    # add notification to self
    def addNotification(self, string):
        self.__notifications.append(string)
        print("notification to " + self.UN + ": " + string)
    def printNotification(self):
        for notific in self.__notifications:
            print(notific)
    def __str__(self):
        return f"User name: {self.UN}, Number of posts: {len(self.__posts)},Number of followers: {len(self.__followers)}"
