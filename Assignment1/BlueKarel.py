from karel.stanfordkarel import *

"""
File: BlueKarel.py
-----------------------
Goal: Karel paints the world blue, then draws a black windowframe. 
"""

def main():
    """
    requires world to be at least 3 wide and tall
    """
    paint_world_blue()
    build_frame()
    build_panes()

def paint_world_blue():
    #pre-condition: bottom west corner, facing east (left is clear)
    #post-condition: top east corner, facing east (left is blocked)
    while left_is_clear():
        paint_row()
        next_row()
    paint_row()

def build_frame():
    #pre: top east corner, facing east
    #post: top east corner, facing east
    turn_around()
    for i in range(4):
        paint_side()
        turn_left()
    return_bottom()
    turn_around()


def build_panes():
    find_midpoint()
    turn_right()
    paint_side()
    return_bottom()
    turn_right()
    find_midpoint()


def paint_side():
    while front_is_clear():
        paint_corner(BLACK)
        move()
    paint_corner(BLACK)

def paint_row():
    paint_corner(BLUE)
    while front_is_clear():
        #pre-condition: front is clear
        #post-condition: front is blocked
        move()
        paint_corner(BLUE)

def next_row():
    #pre-condition:
    #post-condition:
    turn_left()
    move()
    turn_left()
    while front_is_clear():
        move()
    turn_around()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

def return_bottom():
    while not_facing_south():
        turn_left()
    while front_is_clear():
        move()
    return_west_wall()

def find_midpoint():
    line_row()
    while right_is_clear():
            # Pre-condition: K is at bottom west wall, facing west
            # Post-condition: K is at bottom west wall, facing west
        check_one()  # Check if there's only 1 beeper left. If yes, end loop.
        check_two()  # Check if there's only 2 beepers left. If yes, pick one, then end loop.
        clear_edges()  # Removes west-most and east-most beepers, then restarts loop.

    return_beeper()  # Returns Karel to Beeper midpoint

def line_row():
        # GOAL: put beeper on every spot except corners
        # Pre-condition: bottom west corner, facing EAST
        # Post-condition: bottom east corner, facing WEST
    while front_is_clear():
        move()
        put_beeper()
    pick_beeper()
    return_west_wall()

def check_one():
        # pre-condition: bottom west corner, facing West. assumes >= 1 beepers to the east of K
        # post-condition: bottom west corner, facing West
    turn_around()
    find_beeper()  # Finds first beeper
    while front_is_clear():
            # Pre-condition: Facing East. Front is clear
            # Post-condition: Facing East. Front is clear
        move()
        if beepers_present():  # Finds second beeper, ends inner loop
            return_west_wall()  # If no beepers present, hits East wall facing east: ends main loop.

def check_two():
        # pre-condition: bottom west corner, facing west. assumes >= 2 beepers to the east of K
        # post-condition: bottom west corner, facing west
    if right_is_clear():
        turn_around()
        find_beeper()  # Finds first beeper
        move()
        find_beeper()  # Finds second beeper
        while front_is_clear():
                # Pre-condition: Facing East. Front is clear
                # Post-condition: Facing East. Front is clear
            move()
            if beepers_present():  # Finds third beeper, ends inner loop
                return_west_wall()
        if right_is_blocked():  # Determines that only two beepers left. Pick one, then end main loop.
            turn_around()
            find_beeper()
            pick_beeper()
            turn_around()
            while front_is_clear():
                move()

def clear_edges():
        # pre-condition: bottom west corner facing west
        # post-condition: bottom west corner facing west
    if right_is_clear():
        clear_east()
        clear_west()
##can be optimized!!!
def clear_east():
    turn_around()
    find_beeper()
    pick_beeper()
    return_west_wall()

def clear_west():
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    find_beeper()
    pick_beeper()
    return_west_wall()

def find_beeper():
        # Pre-condition: not on a beeper, facing East
        # Post-condition: on a beeper, facing East
    while no_beepers_present():
        move()

def return_west_wall():
    while not_facing_west():
        turn_left()
    while front_is_clear():
        move()

def return_beeper():
        # pre-condition: top west corner, facing west. midpoint beeper is only remaining beeper.
        # post-condition: bottom row, on midpoint beeper.
    turn_around()
    find_beeper()
    pick_beeper()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
