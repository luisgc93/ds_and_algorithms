"""
The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.
For example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity checks are
used to detect single bit errors in data storage and communication. It is fairly
straightforward to write code that computes the parity of a single 64-bit word. How would
you compute the parity of a very large number of 64-bit words?
Hint: Use a lookup table, but don't use 264 entries!

REMINDER - BITWISE OPERATORS:
~ 1s COMPLEMENT (flip bits but remember about the sign bit - 0 for positive and 1 for
negative), also 2s complement = 1s complement + 1)
CONTINUE: https://www.bbc.co.uk/bitesize/guides/zjfgjxs/revision/5 - THEN WORK ON IMPROVING PARITY METHOD
& BITWISE AND
| BITWISE OR
>> BIT SHIFT

CONVERTING TO/FROM BINARY
In [1]: bin(12)
Out[1]: '0b1100'

In [2]: int('0b1100', 2)
Out[2]: 12
"""


def compute_parity(x: int):
    number_of_ones = 0
    while x:
        number_of_ones += x & 1
        x >>= 1

    return int(number_of_ones % 2 != 0)
