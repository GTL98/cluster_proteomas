from functools import wraps


def memoize(funcao):
    cache = {}

    @wraps(funcao)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = funcao(*args, **kwargs)
        return cache[key]
    return wrapper
