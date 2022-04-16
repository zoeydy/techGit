
# Using + and * with Sequences

from re import T


l = [1, 2, 3]
l * 5
5 * 'abcd'
[[1, 2, 3]] * 3

# 1.building list of list
# E.g.2-13 A list with three lists of length 3 can represent a tic-tac-toe board
board = [['_'] * 3 for i in range(3)]
board
board[1][2] = 'x'
board

# E.g.2-14 !pitfall! A list with three references to the same list is useless
weird_board = [['_']*3]*3
weird_board
board == weird_board
weird_board[1][2] = '0'
weird_board

# the weird_board is the same as
row = ['_']*3
why = []
for i in range(3):
    why.append(row) # instead of append different list
why == [['_']*3]*3

norm = []
for i in range(3):
    row = ['_'] * 3
    norm.append(row)
norm == board

# although
norm == why
# when asigning values:
why[1][2] = 'why'
why
norm[1][2] = 'norm'
norm




# 2. Augmented Assignment with Sequences += *=
l = [1,2,3]
id(l)
l *= 2
l
id(l)

t = (1,2,3)
id(t)
t *= 2
t 
id(t)

# e.g.2-16 The unexpected result: item t2 is changed and an exception is raised
t = (1,2,[30,40])
try:
    t[2] += [50,60]
except:
    print(t)


# e.g.2-17 Bytecode for the expression s[a] += b
# dis.dis('s[a] += b')