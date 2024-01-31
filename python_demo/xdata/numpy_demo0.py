"""
pip install numpy

https://numpy.org/doc/
"""


import numpy as np


array = np.array([1, 2, 3])
# array.shape=(3,), array.ndim=1, array.size=3, array.dtype=dtype('int32')
print(f"{array.shape=}, {array.ndim=}, {array.size=}, {array.dtype=}")

array = np.array([
    [1, 2, 3],
    [11, 22, 33],
])
# array.shape=(2, 3), array.ndim=2, array.size=6, array.dtype=dtype('int32')
print(f"{array.shape=}, {array.ndim=}, {array.size=}, {array.dtype=}")