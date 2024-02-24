from User import User

# This class is a Singleton factory of users.
# Only one instance is allowed

class SocialNetwork:
    __instance = None
    __initialized = False
    def __init__(self, name):
        if not SocialNetwork.__initialized:
            self.__name = name
            # creating a dict of users for FlyWeight pattern benefits
            self.__users = {}
            SocialNetwork.__initialized = True
            print("The social network " + name + " was created!")
            SocialNetwork.__instance = self
        else:
            self.__dict__ = SocialNetwork.__instance.__dict__
            raise SingletonException("Only one SocialNetwork Object is allowed!")

    def sign_up(self, UN, PW):
        if UN in self.__users:
            # make sure only one user with the same name exist a all time.
            raise InvalidInputException("UserName already exist in " + self.__name + " Existing user has been returned!")
            return self.__users[UN]
        if len(PW) > 8 or len(PW) < 4:
            raise InvalidInputException("Password must be of 4 to 8 characters! No user was signed up!")
        self.__users[UN] = User(UN, PW)
        return self.__users[UN]
    def log_in(self, UN, PW):
        self.__users[UN].login(PW)
    def log_out(self, UN):
        self.__users[UN].logout()
    def __str__(self):
        ans = self.__name + " social network:\n"
        for user in self.__users.values():
            ans = ans + str(user) + "\n"
        return ans
class SingletonException(Exception):
    pass
class InvalidInputException(Exception):
    pass