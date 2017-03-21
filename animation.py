#!/usr/bin/env python

from visual import *

# initialize "earth" object attributes (arbitrary for now)
earth = sphere()
earth.pos = vector(2,4,0)
earth.radius = .5
earth.color = color.blue

#initialize "sun" object attributes (arbitrary for now)
sun = sphere()
sun.pos = vector(0,0,0)
sun.radius = 1
sun.color = color.orange

# set initial velocity as downwards
earth.velocity = vector(0,-1,0)
dt = 0.01

while 1:                         # run forever
    rate (100)                   # specifies max executions per second

    # caluclate new position with  distance = prev distance + rate*time
    earth.pos = earth.pos + earth.velocity*dt

    if earth.y < earth.radius:                        # bounce back up
        earth.velocity.y = abs(earth.velocity.y)
    else:
        # new velocity from equation v = v0 + a*time where a is -9.8 (gravity)
        earth.velocity.y = earth.velocity.y - 9.8*dt
