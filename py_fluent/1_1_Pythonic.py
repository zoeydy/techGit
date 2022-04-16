
# using special methods to leverage the Python Data Model:
# E.g. 1-1 deck as a sequence of playing cards
# 创建class
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

# 创建objects/实例？instance
beer_card = Card('7', 'diamonds')      
beer_card

deck = FrenchDeck()
len(deck)

# using special methods
deck[0]
deck[-1]

from random import choice
choice(deck)
choice(deck)
choice(deck)

deck[:3]
deck[12::13]

for card in deck:
    print(card)
for card in reversed(deck):
    print(card)


# if a collection does not have __contains__ method, the in operator does a sequential scan
Card('Q', 'hearts') in deck
Card('7', 'beasts') in deck

# sorting
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)




# How special methods are used
# 1.Emulating Numeric Types: __add__ __mul__
# TODO: error: name 'Vector' is not defined
# v1 = Vector(2, 4) 
# v2 = Vector(2, 1) 
# v1 + v2

# E.g. 1-2 A simple two-dimensional vector class
"""
vector2d.py: a simplistic class demonstrating some special methods

It is simplistic for didactic reasons. It lacks proper error handling,
especially in the ``__add__`` and ``__mul__`` methods.

This example is greatly expanded later in the book.

Addition::
    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)
Absolute value::
    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0
Scalar multiplication::
    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0
"""

import math
class Vector:
    def __init__(self):
        self.x = x 
        self.y = y 
    
    def __repr__(self) -> str:
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# 2.String representation of objects __repr__


# 3.Boolean value of an object
# 4.Implementing collections