

# Tuples Are Not Just Immutable Lists
# they also works as records with no field names

# 1.tuples used as records
# e.g. 2-7 tuples used as records
from concurrent.futures.process import _threads_wakeups
import sys
from copy import copy

from attr import has


lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s %s' %passport)
for country,_ in traveler_ids: # unpacking
    print(country, _) # _: dummy variable



# 2.Tuples as Immutable Lists
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])

try:
    b[-1] = [1,2,99]
    print(b)
except:
    print(sys.stderr)

b[-1].append(99)
a == b

# an object is only hashable if its value cannot ever change
def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tf = (10, 'alpha', (1, 2)) 
tm = (10, 'alpha', [1, 2])

fixed(tf)
fixed(tm)
