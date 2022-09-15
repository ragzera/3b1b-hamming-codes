import numpy as np
from functools import reduce
import operator as op

# TODO: Actually implement the Hamming parity checks and make sure they work

bits = np.random.randint(0,2,11) # Generate a random 11-bit block
print("bits: ${bits}")



# res = reduce(op.xor, [i for i, bit in enumerate(bits) if bit])
# print("Culprit: ${res}")
# res = reduce(lambda x,y: x ^ y, [i for i, bit in enumerate(bits) if bit])
