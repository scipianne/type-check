import inspect
from functools import wraps


def type_check():
    """Decorator for type-checking parameters of the function"""

    def decorator(func):

        @wraps(func)
        def check_types(*args, **kwargs):
            args_names = inspect.getfullargspec(func).args
            annotations = inspect.getfullargspec(func).annotations
            types = list(annotations.values())
            return_type = None
            if 'return' in annotations:
                return_type = annotations['return']
                types = types[1:]

            for argument, type in zip((args), types):
                if not isinstance(argument, type) and argument is not None:
                    raise TypeError("{} should be a {} instance".format(argument, type))

            for keyword in kwargs:
                argument = kwargs[keyword]
                type = types[args_names.index(keyword)]
                if not isinstance(argument, type) and argument is not None:
                    raise TypeError("{} should be a {} instance".format(argument, type))

            result = func(*args, **kwargs)
            if return_type is not None and not isinstance(result, return_type):
                raise TypeError("{} should be a {} instance".format(result, return_type))

            return result

        return check_types

    return decorator
