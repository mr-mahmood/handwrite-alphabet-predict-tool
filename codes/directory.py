import os


def add():
    # Get the directory of the current script and go to mnist images directory
    ADDRESS = os.path.dirname(os.path.abspath(__file__))
    ADDRESS = list(ADDRESS)
    ADDRESS[2] = "/"
    ADDRESS[len(ADDRESS)-6:len(ADDRESS)] = "/"
    ADDRESS = ''.join(ADDRESS)
    
    return ADDRESS


hand_write_English_alphabet = 'files/neural network/English alphabet.h5'