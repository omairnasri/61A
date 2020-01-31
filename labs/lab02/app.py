from numpy import *
import numpy as np

i = 0
a = []

while i < 30:
    s = 2**i
    a.append(log10(s))
    i += 1