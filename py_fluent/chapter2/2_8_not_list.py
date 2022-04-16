


# 1. Arrays
# e.g.2-18. Creating, saving, and loading a large array of floats
from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
floats[-1]

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
floats2[-1]

floats2 == floats


# 2. Memory Views (class)
# e.g. 2-19Handling 6 bytes memory of as 1×6, 2×3, and 3×2 views
from array import array
octets = array('B', range(6))
m1 = memoryview(octets)
m1.tolist()
m2 = m1.cast('B', [2,3])
m2.tolist()
m3 = m1.cast('B', [3,2])
m3.tolist()
m2[1,1] = 22
m3[1,1] = 33
octets # the memory was shared among octets, m1, m2, and m3

# e.g.2-20. Changing the value of an 16-bit integer array item by poking one of its bytes
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
len(memv)
memv[0]
memv_oct = memv.cast('B')
memv_oct.tolist()
memv_oct[5] = 4
numbers



# 3.Numpy
# e.g.2-21. Basic operations with rows and columns in a numpy.ndarray
import numpy as np
a = np.arange(12)
a
type(a)
a.shape
a.shape = 3,4
a
a[2]
a[2,1]
a[:,1]
a.transpose()

# TODO: loadtxt 找不到文件？
# floats = np.loadtxt('floats-10M-lines.txt')
# floats[-3:]
# floats *= .5
# floats[-3:]
# from time import perf_counter as pc
# t0 = pc(); floats /= 3; pc() - t0
# np.save('floats-10M', floats)
# floats2 = numpy.load('floats-10M.npy', 'r+')
# floats2 *= 6
# floats2[-3:]

# 4.Deques and other queues
# e.g.2-22. Working with a deque
from collections import deque
dq = deque(range(10), maxlen = 10)
dq
dq.rotate(3)
dq
dq.rotate(-4)
dq
dq.appendleft(-1)
dq
dq.extend([11,22,33])
dq
dq.extendleft([10,20,30,40])
dq