"""
Estimates pi using a Monte Carlo method: Generate random points on the xy-plane, with x and y
coordinates uniformly distributed in the range [0, 1), then count the fraction of the points that
are within the unit circle x^2 + y^2 <= 1. The estimated value of pi is this fraction multiplied
by 4.
Syntax: python estimate-pi.py <number of points>
"""

import random
import sys

num_points = int(sys.argv[1])
inside_circle = 0
for i in range(num_points):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        inside_circle += 1

pct_inside_circle = inside_circle / num_points
print(pct_inside_circle * 4)