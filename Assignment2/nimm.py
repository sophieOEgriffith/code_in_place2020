"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    """
    1. Start w/ pile of 20 stones
    2. Alternate between player1 and player2
    3. Each player takes either 1 or 2 stones from the pile
    4. When there are 0 stones left, the game is over.
    5. Player whose turn it *isn't* wins
    """
    pile = 20
    turn = 1

    while pile > 0:
        print("There are " + str(pile) + " stones left.")
        stones = int(float(input("Player " + str(turn) + " would you like to remove 1 or 2 stones? ")))
        if stones != 2 and stones != 1:
            print("You can't take that many! Try again!")
        else:
            pile -= stones
            if turn == 1:
                turn = 2
            else:
                turn = 1
    print("Player " + str(turn) + " wins!")






# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
