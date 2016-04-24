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
    if (len(ASCII_list) % dimension):
        for i in range(dimension - (len(ASCII_list) % dimension)):
            ASCII_list.append(32)

    # Convert list into matrix with given dimension
    ASCII_array = np.array(ASCII_list)
    size = (len(ASCII_list) / dimension), dimension  #height, width
    return np.reshape(ASCII_array, size).T

def matrix_to_string(matrix, dimension):
    '''
    Converts an input matrix to a string of characters
    '''
    # Initizialize a list of ASCII values
    ASCII_list = []

    # Convert matrix into a list / Operate over each element in each row
    for element in matrix.T.tolist():
        for d in range(dimension):
            ASCII_list.append(element[d])

    # Convert list of ASCII values to characters
    plain_characters = [chr(character) for character in ASCII_list]
    
    # Combine list into comprehensible string
    plaintext = ''.join(plain_characters)
    
    return plaintext

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

    #map each letter to a number
    character_array = string_to_matrix(plaintext, dimension)

    #matrix operation on the number
    encoded_array = np.dot(key, character_array)

    #convert matrix to ciphertext
    ciphertext = matrix_to_string(encoded_array)

    return ciphertext, key



def decipher(ciphertext, key, dimension=2):
    '''
    Deciphers into plaintext
    '''
    pass

