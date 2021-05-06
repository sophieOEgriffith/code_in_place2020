"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random
RAND_MIN = 10
RAND_MAX = 99
GOAL = 3

def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    correct = 0

    while correct < GOAL:
        #random.seed(1)
        ##set up addition problem:
        num1 = random.randint(RAND_MIN, RAND_MAX)
        num2 = random.randint(RAND_MIN, RAND_MAX)
        ans = num1 + num2

        ##print and solve addition problem:
        print("What is " + str(num1) + " + " + str(num2) + "?")
        attempt = int(input("Your answer: "))
        if attempt == ans:
            correct += 1
            print("Correct! You've gotten " + str(correct) + " correct in a row.")
        else:
            correct = 0
            print("Incorrect. The expected answer is " + str(ans))

    print("Congratulations! You've mastered addition!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
