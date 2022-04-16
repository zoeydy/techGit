from cgi import print_arguments
import sys
import os
import this

from pyparsing import col


# e.g.1 list comprehension *last*
x = 'abc'
codes = [ord(x) for x in x]
print(x)
print(codes)
lasts = [last := ord(temp) for temp in x]
print(lasts)

# ***
print(last)
try:
    print(temp)
except:
    print(sys.stderr)




# e.g.2 use `map` and `filter`
symbols = '$¢£¥€¤'

# 1.use traditional comprehension
ascii1 = [ord(d) for d in symbols if ord(d) > 127]
print(ascii1)

# 2.use map and filter
ascii2 = list(filter(lambda d: d > 127, map(ord, symbols)))
print(ascii2)

print(ascii1==ascii2)




# 3.e.g. Cartesian product using a list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirt_cs = [(color, size) for color in colors for size in sizes]
tshirt_sc = [(color, size) for size in sizes for color in colors]

print(tshirt_cs)
print(tshirt_sc)



# Generator Expressions
symbols = '$¢£¥€¤'
tuple(ord(i) for i in symbols)
import array
array.array('i', (ord(i) for i in symbols))

# e.g. 2-6 if the list is too big, genexp can save the cost of building a list with a million items just to feed the for loop
for tshirt in(f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)

for c in colors:
    for s in sizes:
        print((c,s))
