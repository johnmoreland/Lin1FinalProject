"""
Code that encodes and deciphers hill ciphers
@authors: John Moreland and Jeremy Garcia
"""

import math
import numpy as np

#chr and ord are our friends

def is_invertible(key):
    '''
    Verifies that the given matrix is is_invertible
    Output: Boolean
    '''
    # Checks if determinant is nonzero
    determinant = np.linalg.det(key)
    return bool(determinant)

def string_to_matrix(plaintext, dimension):
    '''
    Converts an input string into a matrix of numbers
    '''
    # Map each character to an ASCII value
    ASCII_list = [ord(char) for char in plaintext]
    
    # Fill in empty elements
    if len(ASCII_list) % dimension:
        for i in range(len(ASCII_list) % dimension):
            ASCII_list.append(32)

    # Convert list into matrix with given dimension
    ASCII_array = np.array(ASCII_list)
    size = (len(ASCII_list) / dimension), dimension  #height, width
    return np.reshape(ASCII_array, size).T



def matrix_to_string(matrix, dimension):
    '''
    converts a matrix to a string
    '''
    pass

def invert_matrix(key):
    '''
    Inverts the input matrix
    '''
    return np.linalg.inv(key)

def generate_key(dimension):
    '''
    Creates a square matrix with given dimensions
    '''
    return np.random.randint(256, size=(dimension,dimension))

def encipher(plaintext, dimension=2):
    '''
    Generates ciphertext from the given plaintext and corresponding key
    '''
    #Create a key if needed,
    key = generate_key(dimension)
    print key

    #check if key is invertible
    is_invertible(key)

    #map each letter to a number
    #string_to_matrix(plaintext, dimension)
 
    #matrix operation on the number

def decipher(ciphertext, key, dimension=2):
    '''
    Deciphers into plaintext
    '''
    pass

print string_to_matrix("jeremy is lame!", 2)
encipher('abcdef')