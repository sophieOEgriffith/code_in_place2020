from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
Goal: place every other spot with a beeper.
1. Line a row w/ beepers on every other spot.
2. Move to next row. Decide where to start the next row.
3. Finish row w/ alternating beepers.
4. Continue until done.
Assumptions: World is empty, Karel starts in bottom left corner.
    """
#Pre-condition: at bottom left corner of empty world, facing east
#Post-condition: at top right corner of checkered world, facing north
    while front_is_clear():
        every_other()
        next_column()



#Goal: Line remainder of the row with beepers on alternating spots
#Pre-condition: Front is clear, no beeper on current spot or previous spot
#Post-condition: End of row, facing wall.
def every_other():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

#Goal: move to the left-most side of the next column up, and adjust for appropriate start of every_other()
###If at final row, stop.
#Pre-condition: At eastern end of a finished row, facing the wall
#Post-condition: Positioned at western end of a row, facing east and adjusted to meet Pre-con for every_other()
def next_column():
    turn_left()
    if front_is_clear():
        move()
        turn_left()
        return_to_wall()
        turn_around()
        check_bottom()

#Goal: place beepers on alternating spots throughout row
#Pre-condition:Standing at one end of row, facing opposite end of row. No beeper on current spot.
#Post condition: At opposite wall, facing wall. May or may not be standing on a beeper
def check_bottom():
    turn_right()
    move()
    if no_beepers_present():
        turn_around()
        move()
        put_beeper()
        turn_right()
        move()
        move()
    else:
        turn_around()
        move()
        turn_right()
        move()

def return_to_wall():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point


if __name__ == "__main__":
    run_karel_program()
