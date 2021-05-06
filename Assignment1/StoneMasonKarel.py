from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""

def main():
    """
    goal: first column, move to next, repeat until done
    """
    #Pre-condition: face East
    #Post-condition: face East
    while front_is_clear():
        build_column()
        next_column()
    build_column()

#Creates a column with beepers. Assumes that column should reach from "ground" to "ceiling"
#Pre-condition: Front is Clear
#Post-condition: Front is Blocked
def build_column():
    face_north()
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
            move()
    if no_beepers_present():
        put_beeper()

#Moves Karel to base of column, then to next column
#Pre-condition: at top of column, facing "ceiling"
#Post-condition: At base of next column, facing east.
def next_column():
    turn_around()
    while front_is_clear():
        move()
    while not_facing_east():
        turn_left()
    for i in range(4):
        move()

def face_north():
#Turns Karel north
#Pre-condition: facing not-north
#Post-condition: facing north
    while not_facing_north():
        turn_left()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
