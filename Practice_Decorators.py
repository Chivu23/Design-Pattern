# ---> DECORATORS <---

# @property
# @abstractmethod

def new_decorator(original_func):  # --> decorator
    # original func = the reference to the function to be decorated

    def wrapper_func():
        # we write code that we want to happen BEFORE calling the function original_func
        print("Some code BEFORE call to the original_func")

        original_func()  # ---> call function original_func

        # we write code that we want to happen AFTER calling the function original_func
        print("Some code AFTER we call the original_func")

    return wrapper_func


@new_decorator
def func_needs_decoration():
    print("I want to be decorated nice and soft")


func_needs_decoration()


@new_decorator
def hello():
    print("Have a nice day and code everyday!")


hello()


# If we apply the decorator to the function below, will it work?

@new_decorator
def combine(name):
    print(f"The power of your smile, is in your thoughts {name}!")


# combine("Maria")


def decorator_combine(original_func):
    def wrapper_func(*args, **kwargs):     # any param
        print(f"inside of the function {original_func.__name__}")

        original_func(*args, **kwargs)

        print(f"outside of the function {original_func.__name__}")

    return wrapper_func


@decorator_combine
def combine(name):
    print(f"Salut, {name}")


combine("Marie")
