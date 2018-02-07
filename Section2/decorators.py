import functools

# def my_decorator(func):
#     @functools.wraps(func)
#     def function_that_runs_func():
#         print("In the decorator!")
#         func()
#         print("After the decorator!")
#     return function_that_runs_func


# @my_decorator
# def my_function():
#     print("I am the function that gets run!!")

# my_function()


## Advanced: the decorator that can take argument itself

def decorator_with_arg(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator")
            if number == 56:
                print("Not running the function!")
            else:
                func()
            print("After the decorator!")
        return function_that_runs_func
    return my_decorator

@decorator_with_arg(56)
def my_function_two(x, y):
    print(x + y)

my_function_two(3, 4)