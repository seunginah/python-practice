from src.decorator_record_calls import record_calls

"""
https://www.pythonmorsels.com/exercises/3ee85ad3481f428d99458b102cbda7c6/submit/1/
I'd like you to write a decorator function that will record the number of times a function is called.
Your decorator function should be called record_calls
"""
@record_calls
def greet(name="World"):
    """Greet someone by their name."""
    print(f"Hello {name}")

for i in range(2):
    greet(name="Seungin")
print(f"greet() was called {greet.call_count} times")

"""
Decorator functions are functions which accept another function 
and return a new version of that function to replace it
So this should be the same thing as what we typed above:
greet = record_calls(greet)
"""
greet = record_calls(greet)
greet('seungin')
greet('jaein')
print(f"greet() was called {greet.call_count} times")

"""
Bonus 1
For the first bonus I'd like you to make sure your decorator function preserves
the name and the docstring, and call signature of the original function.

So if we use record_calls on this greet function:
When we ask for help on that function, we should see something like this:
"""
help(greet)
greet('seungin')

"""
Bonus 2: For the second bonus I'd like you to keep track of a calls attribute
on our function that records the arguments and keyword arguments provided for 
each call to our function.
"""

"""
Bonus 3: For the third bonus, add a return_value attribute and an exception 
attribute to each of the objects in our calls list. If the function returned
successfully, return_value will contain the return value. Otherwise, exception
will contain the exception raised.

When an exception is raised, return_value should be set to a special 
NO_RETURN value. Your module should have a NO_RETURN attribute that
contains this special value.
"""