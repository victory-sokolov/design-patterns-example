import logging
from functools import wraps

class Borg:

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)


x = Singleton(HTTP="Hyper Text Transfer")
y = Singleton(HTTP="Hyper Text Transfer2")
z = Singleton(HTTP="Hyper Text Transfer3")

# singleton


def singleton(_class):
    instances = {}

    @wraps(_class)
    def wrapper(*args, **kwargs):
        if _class not in instances:
            instances[_class] = _class(*args, **kwargs)
        return instances[_class]
    return wrapper


@singleton
class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)


cls = MyClass("Viktor")
cls2 = MyClass("Artem")
cls3= MyClass("Roma")
print(cls)
print(cls2)
print(cls3)
