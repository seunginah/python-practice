"""
https://www.pythonmorsels.com/exercises/ded322173d47424581be45adaeeca90d/?level=advanced
I'd like you to create a context manager. Context managers use a with block to
bookend a block of code with automatic setup and tear down steps.

What I mean by "suppress" is that if the given exception type is raised,
that exception should be caught and muted in a sense. As is common in other
exception-handling in Python, child classes of the given exception type should
be caught and muted as well. To solve this exercise, you'll want to lookup
how to create a context manager in Python.

Your context manager, suppress, should suppress exceptions of a given type:
with suppress(NameError):
    print("Hi!")
    print("It's nice to meet you,", name)
    print("Goodbye!")

> Hi!


x = 0
with suppress(ValueError):
    x = int('hello')

x
> 0

But exceptions of other types shouldn't be suppressed (we're suppressing a TypeError and a NameError is raised):

with suppress(TypeError):
    print("Hi!")
    print("It's nice to meet you,", name)
    print("Goodbye!")

Hi!
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
NameError: name 'name' is not defined
"""