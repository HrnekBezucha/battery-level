#!/usr/bin/python3
"""
    Utility for Linux systems which takes battery charge from
    BAT0 and displays a number of hearts or dots.
    To be used by tmux or conky.
"""

max_points = 5
point_value = 20            # full charge / max_points
points = []

full_heart = "♥"
empty_heart = "♡"           # double-width symbol.. *sigh*
full_dot = "•"
empty_dot = "○"

full_point = full_dot       # choose symbol hearts or dots
empty_point = empty_dot


with open("/sys/class/power_supply/BAT0/capacity", 'r') as f:
    """ Reads data from battery driver file."""
    charge = int(f.read())


for point in range(max_points):
    """Prints full point if divisible by point_value
        or empty if not."""
#   no reason to print when full charge
    if charge > 95:
        break
    elif charge // point_value:
        points.append(full_point)
        charge = charge - point_value
    else:
        points.append(empty_point)
        break

print(*points)

