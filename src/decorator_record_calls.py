from typing import NamedTuple
from functools import wraps

NO_RETURN = None

class Call:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

# Alternative solution to class Call: create a named tuple
# Alt 1:
# Call = namedtuple('Call', 'args kwargs')
"""
Alt 2:
class Call(NamedTuple):
    args: tuple
    kwargs: dict
"""

def record_calls(func):
    """
    Record the number of times a function is called
    :param func: function with positional or keyword args
    :return: decorated function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        wrapper.calls.append(Call(args, kwargs))
        return func(*args, **kwargs)
    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper

