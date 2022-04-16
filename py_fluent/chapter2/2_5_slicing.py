

l = [10, 20, 30, 40, 50, 60]
l[:2]
l[2:]
l[:3]
l[3:]

# stride to skip
s = 'bicycle'
s[::3]
# stride to reverse
s[::-1]
# stride to reverse and skip
s[::-2]


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

deck = FrenchDeck()
deck[12::13]

# seq[start:stop:step]

# E.g.2-12 Line items from a flat-file invoice
invoice = """
... 0.....6.................................40........52...55........
 ... 1909 Pimoroni PiBrella $52.50
... 1489 6mm Tactile Switch x20 $9.90
... 1510 Panavise Jr. - PV-201 $28.00
... 1601 PiTFT Mini Kit 320x240 $34.95
... """

SKU = slice(0,6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])


# Multidimensional Slicing and Ellipsis
l = list(range(10))
l
l[2:5] = [20,30]
l
del l[5:7]
l
l[3::2] = [11,22]
l
l[2:5] = [100]
l