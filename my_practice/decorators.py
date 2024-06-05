# Task: "Decorator @retry"
# Write a decorator @retry that will retry a function a given number of times
# if it raises an exception. The decorator should accept two arguments: the
# number of attempts and the delay between attempts in seconds.

# Декоратор с аргументами


import random
import time


def retry(attempts=0, delay=0):
    def wrapper(func):
        def inner(*args, **kwargs):

            count = attempts
            while count > 0:

                try:
                    return func(*args, **kwargs)

                except Exception as e:
                    print(f'Exeption: {e}, retrying in {delay} seconds...')
                    time.sleep(delay)
                    count -= 1
            return func(*args, **kwargs)

        return inner

    return wrapper


# Example usage:


@retry(attempts=3, delay=2)
def unstable_function():
    if random.choice([True, False]):
        print("Success!")
    else:
        print("Fail!")
        raise ValueError("Something went wrong")


# unstable_function()


# Task: "Decorator @log_calls"
# Write a decorator with parameters that logs function calls. The decorator
# should accept two parameters: the name of the log file and the logging level
# (e.g., "INFO", "DEBUG", "ERROR"). When the decorated function is called,
# the decorator should write a message to the specified file with the logging
# level and information about the function call (function name and arguments).
#
# Example usage:
#
# @log_calls("log.txt", "INFO")
# def my_function(a, b):
#     return a + b
#
# my_function(2, 3)
#
# The "log.txt" file should contain something like:
# INFO: Called my_function with args: (2, 3), kwargs: {}

# Логирование в файл, построение пути, дандер метод, dunder methods,
# double underscores


import logging  # noqa E402
import os  # noqa E402


def log_calls(file_name, level):
    def wrapper(func):
        logging.basicConfig(filename=file_name, level=getattr(logging, level))

        def inner(*args, **kwargs):
            logging.log(
                getattr(logging, level),
                f'Called {func.__name__} with args: {args}, kwargs: {kwargs}'
            )
            return func(*args, **kwargs)

        return inner

    return wrapper


logfile = os.path.join(
    os.path.dirname(__file__), '..', 'tests', 'fixtures', 'log.txt'
)


@log_calls(logfile, "INFO")
def sum(a, b):
    return a + b

# print(sum(1, 2))
