"""
Code that encodes and deciphers hill ciphers
@authors: John Moreland and Jeremy Garcia
"""

import math
import numpy as np

#chr and ord are our friends

def is_invertible(matrix):
    '''
    Verifies that the given matrix is is_invertible
    Output: Boolean
    '''
    # Checks if determinant is nonzero
    determinant = np.linalg.det(matrix)
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
    ASCII_array = np.array(ASCII_list, dtype=int)
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

def invert_matrix(matrix):
    '''
    Inverts the input matrix
    '''
    matrix = (np.linalg.inv(matrix))
    # det = -1/np.linalg.det(matrix)
    # matrix = np.multiply(matrix,det)
    # matrix = matrix.astype(int)
    # matrix = np.mod(matrix,128)
    return matrix

def generate_key(dimension):
    '''
    Creates a square matrix with given dimensions
    '''
    # key = np.random.randint(256, size=(dimension,dimension))
    # if is_invertible(key):
    # 	key = np.mod(key,128)
    # 	return key
    # #if not invertible, generate a new key
    # return generate_key(dimension)

    if dimension == 2:
    	key = np.array([[1, 2],[2, 3]])
    elif dimension ==3:
    	key = np.array([[7,2,1],[0,3,-1],[-3,4,-2]])
    return key

def encipher(plaintext, dimension=2):
    '''
    Generates ciphertext from the given plaintext and corresponding key
    '''
    #Create a key
    key = generate_key(dimension)

    #map each letter to a number
    character_array = string_to_matrix(plaintext, dimension)

    #matrix operation on the number
    encoded_array = np.dot(key, character_array)
    modded_array = np.mod(encoded_array, 128)

    #convert matrix to ciphertext
    ciphertext = matrix_to_string(modded_array, dimension)
    return ciphertext, key

def decipher(ciphertext, key, dimension=2):
    '''
    Deciphers into plaintext
    '''
    #invert the key
    decipher_key = invert_matrix(key)

    #convert ciphertext to character array
    ciphertext_array = string_to_matrix(ciphertext, dimension)

    #matrix operation on array
    decoded_array = np.dot(decipher_key, ciphertext_array)
    modded_array = np.mod(decoded_array,128)
    rounded_array = np.rint(modded_array)
    new = rounded_array.astype(int)
    #convert new character array back to string
    plaintext = matrix_to_string(new, dimension)
    return plaintext

ciphertext, key = encipher('jeremy is awesome',2)
print 'ciphertext:',ciphertext
print key
print invert_matrix(key)
print 'deciphered:',decipher(ciphertext,key,2)
