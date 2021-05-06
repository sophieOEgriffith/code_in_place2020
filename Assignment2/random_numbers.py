"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100

def main():
    """
    Prints out a sequence of random numbers. Can set length of sequence and range of random numbers.
    """

    #random.seed(1)
    for i in range(NUM_RANDOM):
        num = random.randint(MIN_RANDOM, MAX_RANDOM)
        cardinal = i + 1
        print("random number " + str(cardinal) + " is " + str(num))




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
