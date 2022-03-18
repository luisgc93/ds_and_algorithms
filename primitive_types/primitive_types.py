"""
*1 byte = 8 bits
*In computing, a word is the natural unit of data used by a particular processor design
(this varies and depends on architecture)

REMINDER - BITWISE OPERATORS:
https://realpython.com/python-bitwise-operators/
~ BITWISE NOT/1s COMPLEMENT (flip bits but remember about the sign bit - 0 for positive and 1 for
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

"""
XOR:
TRUE TRUE - FALSE
FALSE TRUE - TRUE
FALSE FALSE - FALSE
TRUE FALSE - TRUE
"""


def parity(x):  # from book
    result = 0
    while x:
        # Notice that they don't do a sum of the result, this is very smart
        result ^= x & 1
        x >>= 1
    return result


def compute_parity(x: int):  # initial version
    number_of_ones = 0
    while x:
        number_of_ones += x & 1
        x >>= 1
    return int(number_of_ones % 2 != 0)

# NOTICE THAT x % 2 == x & 1


def count_bits_that_are_set_to_one(x):
    number_of_bits_set_to_one = 0
    while x:
        number_of_bits_set_to_one += x & 1
        x >>= 1

    return number_of_bits_set_to_one
