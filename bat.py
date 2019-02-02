#!/usr/bin/python3

# get number from /sys/class/power_supply/BAT0/capacity

charge = 90                 # example value
max_points = 5
point_value = 20            # full charge / max_points
points = []

full_heart = "♥"
empty_heart = "♡"           # double-width.. *sigh*
full_dot = "•"              # dots may be better
empty_dot = "○"

full_point = full_dot       # choose symbol hearts or dots
empty_point = empty_dot

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

