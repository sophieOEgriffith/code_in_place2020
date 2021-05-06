from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
-Assumes that Karel's world is at least three corners wide.
-Places a beeper in the central corner (odd world) or one of two central corners (even world).
    -Starts by placing a beeper on every corner except the two adjacent to the wall.
    -In a loop, removes the two outermost beeper
"""

def main():
    line_row()                      #Place beepers all along bottom row, except in corners
    while right_is_clear():
        #Pre-condition: K is at bottom west wall, facing west
        #Post-condition: K is at bottom west wall, facing west

        check_one()                 #Check if there's only 1 beeper left. If yes, end loop.
        check_two()                 #Check if there's only 2 beepers left. If yes, pick one, then end loop.
        clear_edges()               #Removes west-most and east-most beepers, then restarts loop.

    return_beeper()                   #Returns Karel to Beeper midpoint


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
    #pre-condition: bottom west corner, facing West. assumes >= 1 beepers to the east of K
    #post-condition: bottom west corner, facing West
    turn_around()
    find_beeper()                       #Finds first beeper
    while front_is_clear():
        #Pre-condition: Facing East. Front is clear
        #Post-condition: Facing East. Front is clear
        move()
        if beepers_present():           #Finds second beeper, ends inner loop
            return_west_wall()          #If no beepers present, hits East wall facing east: ends main loop.

def check_two():
    #pre-condition: bottom west corner, facing west. assumes >= 2 beepers to the east of K
    #post-condition: bottom west corner, facing west
    if right_is_clear():
        turn_around()
        find_beeper()                   #Finds first beeper
        move()
        find_beeper()                   #Finds second beeper
        while front_is_clear():
            # Pre-condition: Facing East. Front is clear
            # Post-condition: Facing East. Front is clear
            move()
            if beepers_present():  # Finds third beeper, ends inner loop
                return_west_wall()
        if right_is_blocked():      #Determines that only two beepers left. Pick one, then end main loop.
            turn_around()
            find_beeper()
            pick_beeper()
            turn_around()
            while front_is_clear():
                move()

def clear_edges():
    #pre-condition: bottom west corner facing west
    #post-condition: bottom west corner facing west
    if right_is_clear():
        clear_east()
        clear_west()




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
    #Pre-condition: not on a beeper, facing East
    #Post-condition: on a beeper, facing East
    while no_beepers_present():
        move()

def return_west_wall():
    while not_facing_west():
        turn_left()
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()

def return_beeper():
    #pre-condition: top west corner, facing west. midpoint beeper is only remaining beeper.
    #post-condition: bottom row, on midpoint beeper.
    turn_around()
    find_beeper()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()