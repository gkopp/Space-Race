#!/usr/bin/env python

from visual import *

earth = sphere (pos=(2,4,0), radius=.5, color=color.blue)
sun = sphere (pos=(0,0,0), radius=1, color=color.orange)
earth.velocity = vector(0,-1,0)
dt = 0.01

while 1:
    rate (100)
    earth.pos = earth.pos + earth.velocity*dt
    if earth.y < earth.radius:
        earth.velocity.y = abs(earth.velocity.y)
    else:
        earth.velocity.y = earth.velocity.y - 9.8*dt
