#!/usr/bin/env python

from visual import *
from visual.controls import *

# Define Sun/Planet attributes
sun = sphere(pos=(0,0,0), radius=7e10, color=color.yellow)
mercury = sphere(pos=(1e11,1e11,0), radius=2e10, color=(.750,.750,.750))
earth = sphere(pos=(2.5e11,1.5e11,0), radius=3.5e10, color=(.408,.545,.769))
jupiter = sphere(pos=(5.5e11,4e11,0), radius=5e10, color=(.847,.620,.570))

# create lists of planets and corresponding relative speeds
speeds = [1, .75, .5]
planets = [mercury, earth, jupiter]

# initialize trail for each planet
for planet in planets:
    planet.trail = curve(color = color.white)

planets = zip(planets, speeds) # aggregate planet names and speeds

dt = 0.01

# perform animation
while True:
    rate(100)         # max of 100 frames/second
    theta = dt*2*pi;
    for planet, speed in planets:
        planet.pos = rotate(planet.pos, speed*theta)
        planet.trail.append(pos=planet.pos)
