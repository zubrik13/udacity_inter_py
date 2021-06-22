import functools
import helper


def check_types(severity=1):
    # step 1: no-op decorator
    if severity == 0:
        return lambda function: function

    # step 2: generic message broker
    def msg_caller(msg):
        if severity == 1:
            print(msg)
        else:
            raise TypeError(msg)

    # step 3:
    def checker(function):
        expected = function.__annotations__
        # check type of annotations
        assert (all(map(lambda exp: isinstance(exp, type), expected.values())))
        if not expected:
            return function

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            bound_arguments = helper.bind_args(function, *args, **kwargs)
            for arg, val in bound_arguments.items():
                if arg not in expected:
                    continue
                if not isinstance(val, expected[arg]):
                    print(f"Bad Argument! Received {arg}={val}, expecting object of type {expected[arg]}")
            retval = function(*args, **kwargs)
            if 'return' in expected and not isinstance(retval, expected['return']):
                print(f"Bad Return Value! Received {retval}, but expected value of type {expected['return']}")
            return retval

        return wrapper

    return checker
