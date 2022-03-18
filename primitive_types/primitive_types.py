"""
*1 byte = 8 bits
*In computing, a word is the natural unit of data used by a particular processor design
(this varies and depends on architecture)

REMINDER - BITWISE OPERATORS:
~ 1s COMPLEMENT (flip bits but remember about the sign bit - 0 for positive and 1 for
negative - this means that a +ve number will always become -ve and vice versa)
& BITWISE AND (check bits, write 1 if both are 1)
| BITWISE OR (check bits, write 1 if any of them is 1)
^ XOR ("Exclusive OR - check bits, write 1 if bits are different)
>> RIGHT BIT SHIFT (remove bits on the left)
>> LEFT BIT SHIFT (add 0s on the right)

CONVERTING TO/FROM BINARY
In [1]: bin(12)
Out[1]: '0b1100'

In [2]: int('0b1100', 2)
Out[2]: 12

The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.
For example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity checks are
used to detect single bit errors in data storage and communication. It is fairly
straightforward to write code that computes the parity of a single 64-bit word. How would
you compute the parity of a very large number of 64-bit words?
Hint: Use a lookup table, but don't use 264 entries!
"""


def compute_parity(x: int):
    number_of_ones = 0
    while x:
        number_of_ones += x & 1
        x >>= 1

    return int(number_of_ones % 2 != 0)
