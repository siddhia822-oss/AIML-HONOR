def output_decorator(parameter):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("##########################")
            print("#", parameter)
            print("# input:", args)

            result = func(*args, **kwargs)

            print("# output:", result)
            print("##########################")

            return result
        return wrapper
    return decorator


@output_decorator("Adding")
def add(a, b):
    return a + b


add(2,2)
add(67,2)
add(34,35)
add(99,1)
