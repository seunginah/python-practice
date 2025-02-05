"""
https://www.pythonmorsels.com/exercises/9655802abaef47c682555c198ee8b641/?level=advanced
I'd like you to write a FuzzyString class which acts like a string,
but does comparisons in a case-insensitive way. For example:

greeting = FuzzyString('Hey TREY!')
greeting == 'hey Trey!'
> True
greeting == 'heyTrey'
> False
greeting
'Hey TREY!'

I'd like you to make sure equality and inequality match case-insensitively
at first. I'd also like you to ensure that the string representations of
your class match Python's string object's default string representations.
"""