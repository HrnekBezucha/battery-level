#!/usr/bin/python3
"""
    Utility for Linux systems which takes battery charge from
    BAT0 and displays a number of hearts or dots.
    To be used by tmux or conky.
"""

max_points = 5
charge = 0                  # default value

full_heart = "♥"
empty_heart = "♡"           # double-width symbol.. *sigh*
full_dot = "•"
empty_dot = "○"

full_point = full_dot       # choose symbol hearts or dots
empty_point = empty_dot


try:
    with open("/sys/class/power_supply/BAT0/capacity", 'r') as f:
        """ Reads data from battery driver file."""
        charge = int(f.read())
except FileNotFoundError:
    print("Battery charge not found.")

points = (charge * max_points) // 100

if charge > 95:
    pass
elif charge == 0:
# default value
    pass
else:
    display = full_point * points + empty_point * (max_points - points)
    print(display)
    #print(full_point * points + empty_point * (max_points - points))

