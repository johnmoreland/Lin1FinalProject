"""
code that decrypts a hill cipher
@authors: John Moreland and Jeremy Garcia
"""
import math
import numpy as np
import hill_cypher as hc

mat = hc.string_to_matrix('DL5Q',2)
print mat
inv = hc.string_to_matrix('the ',2)
print inv