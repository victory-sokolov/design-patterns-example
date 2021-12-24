from abc import ABC, abstractmethod

class User:
    def __init__(self):
        self.id = 1
        self.name = 'Viktor'
        self.email = 'viktor@gmail.com'


class CheckUser(ABC):
    def __init__(self):
        self.next_check = None

    @abstractmethod
    def check(self, user: User):
        raise NotImplementedError

    def then(self, check):
        self.next_check = check

    def next(self, user: User):
        if self.next_check:
            self.next_check.check(user)
        return

class CheckId(CheckUser):
    def check(self, user: User):
        if(not user.id):
            raise Exception(f"User id not found")

        self.next(user)

class CheckName(CheckUser):
    def check(self, user: User):
        if(not user.name):
            raise Exception(f"User name not found")

        self.next(user)

class CheckEmail(CheckUser):
    def check(self, user: User):
        if(not user.email):
            raise Exception(f"User email not found")

        self.next(user)


user = User()
check_id = CheckId()
check_name = CheckName()
check_email = CheckEmail()

check_id.then(check_name)
check_name.then(check_email)

check_id.check(user)
