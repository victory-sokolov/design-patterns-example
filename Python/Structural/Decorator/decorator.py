from functools import wraps

def heading(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func()
        return f"<h1>{ret}</h1>"
    return wrapper


@heading
def hello_world():
    return "Hello world"

res = hello_world()
print(res)
