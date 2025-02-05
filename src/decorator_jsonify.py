"""
https://www.pythonmorsels.com/exercises/009804ee5e0f4101ad026e1e38657bea/?level=advanced

Make a jsonify decorator that will take the return value of a decorated
function and return a JSON-encoded version of that return value.

@jsonify
def make_user(id, options):
    return {'id': id, 'live': False, 'options': options}

make_user(4, options=None)
> '{"id": 4, "live": false, "options": null}'

Assume that the return value will only consist of these object types
(and containing objects will be of these types as well): Dictionaries,
Lists, Strings, Numbers, Booleans, None
"""