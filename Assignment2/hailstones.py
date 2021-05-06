"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():
    """
    From the Hailstones problem in "Godel, Escher, Bach"
    """
    number = int(input("Enter a number: "))
    count = 0

    while number != 1:
        if number % 2 == 0:
            print(str(number) + " is even, so I take half: " + str(number//2))
            number = number // 2
            count += 1
        else:
            print(str(number) + " is odd, so I make 3n + 1: " + str(3*number + 1))
            number = 3*number + 1
            count += 1
    print("The process took " + str(count) + " steps to reach 1")



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
