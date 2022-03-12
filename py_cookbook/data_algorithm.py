

import imp
from statistics import mean

from matplotlib.pyplot import cla


p = (4,5)
x, y = p
x 
y 

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]

name, shares, price, date = data
name
date

name, shares, price, (year, mon, day) = data
year

(t,e,s,i),shares, price, (year, mon, day) = data
t 
e 
s 
i

# discard
_, shares, price, _ = data
shares
price

# "*"
grades = [3,4,5,6,7,8,9,2,3]
def drop_first_last(grades):
    first, *middle, last = grades 
    return sum(middle)/len(middle)
drop_first_last(grades)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212', 'address') 
name, email, *phone_numbers, address = record

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
trailing
current

# 
records = [
         ('foo', 1, 2),
         ('bar', 'hello'),
         ('foo', 3, 4),
    ]
def do_foo(x, y): 
    print('foo', x, y)
def do_bar(s): 
    print('bar', s)
for tag, *args in records: 
    if tag == 'foo':
        do_foo(*args) 
    elif tag == 'bar':
        do_bar(*args)
for tag, *args in records:
    print(f"{tag} {args}")

# 
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false' 
uname, *fields, homedir, sh = line.split(':')

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
(t,e,s,_),*_ = record

items = [1, 10, 7, 4, 5, 9]
head, *tail = items

# 
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

# 3. keeping the last N items (deque())
from collections import deque

def search(lines, pattern, history=5): 
    previous_lines = deque(maxlen=history) 
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# if __name__ == '__main__':
#     with open('somefile.txt') as f:
#         for line, prevlines in search(f, 'python', 5): 
#             for pline in prevlines:
#                 print(pline, end='') 
#             print(line, end='') 
#             print('-'*20)

q = [1,2,3]
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q
q.append(5)
q

# 复杂度比insert()或list.append() 小
q = deque() 
q.append(1) 
q.append(2) 
q.append(3) 
q
q.appendleft(4)
q
q.pop()
q
q.popleft()
q


# 4. Finding the Largest or Smallest N Items (heapq())
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2] 
print(heapq.nlargest(3, nums)) 
print(heapq.nsmallest(3, nums))

portfolio = [
       {'name': 'IBM', 'shares': 100, 'price': 91.1},
       {'name': 'AAPL', 'shares': 50, 'price': 543.22},
       {'name': 'FB', 'shares': 200, 'price': 21.09},
       {'name': 'HPQ', 'shares': 35, 'price': 31.75},
       {'name': 'YHOO', 'shares': 45, 'price': 16.35},
       {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key = lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key = lambda s: s['price'])

# 
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(nums)
nums
heapq.heappop(nums)
heapq.heappop(nums)
heapq.heappop(nums)

# 5. implementing a priority queue
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
    
q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('apam'), 4)
q.push(Item('grok'), 1)
q.pop()
q.pop()
q.pop()
q.pop()

