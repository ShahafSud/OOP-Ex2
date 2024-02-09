from User import User
class SocialNetwork:
    __numNetworks = 0
    __instance = None
    def __init__(self, name):
        if SocialNetwork.__numNetworks>=1:
            return SocialNetwork.__instance
        self.__name=name
        print("The social network " + name + "was created!")
        self.__users = {}
        SocialNetwork.__numNetworks += 1

    def sign_up(self, UN, PW):
        if len(PW)>8 or len(PW)<4:
            return
        try:
            a = self.__users[UN]
            return
        except Exception as e:
            self.__users[UN] = User(UN, PW)
