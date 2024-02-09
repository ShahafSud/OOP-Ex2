from User import User

class SocialNetwork:
    __initialized = False

    def __init__(self, name):
        if not SocialNetwork.__initialized:
            self.__name = name
            self.__users = {}
            SocialNetwork.__initialized = True
            print("The social network " + name + " was created!")

    def sign_up(self, UN, PW):
        if len(PW) > 8 or len(PW) < 4 or UN in self.__users:
            return None
        self.__users[UN] = User(UN, PW)
        return self.__users[UN]
    def log_in(self, UN, PW):
        self.__users[UN].login(PW)
    def log_out(self, UN):
        self.__users[UN].logout()
    def __str__(self):
        ans = self.__name + "social network:\n"
        for user in self.__users.values():
            ans = ans + str(user) + "\n"
        return ans
