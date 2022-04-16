

# 1.dictionary comprehensions (dictcomp)

# e.g.3-1. Examples of dict comprehensions


dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

country_dial = {country: code for code, country in dial_codes}
country_dial
{code: country.upper()
    for country, code in sorted(country_dial.items())
    if code < 70}


# 2.unpacking mappings
def dump(**kwargs):
    return kwargs
dump(**{'x': 1}, y=2, **{'z':3})
{'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}}

# 3.merging mappings with |
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
d1 | d2

d1
d1 |= d2
d1

# 4. Pattern Matching with Mappings
# e.g.3-2. creator.py: get_creators() extracts names of creators from media records.
def get_creators(records: dict) -> list:
    match records:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return name 
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}: 
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')

b1 = dict(api=1, author='Douglas Hofstadter', 
          type='book', title='Gödel, Escher, Bach')
get_creators(b1)

from collections import OrderedDict
b2 = OrderedDict(api=2, type='book',
        title = 'Python in a Nutshell',
        authors = 'Martelli Ravenscroft Holden'.split())
get_creators(b2)

get_creators({'type': 'book', 'pages': 770})
get_creators('Spam, spam, spam')