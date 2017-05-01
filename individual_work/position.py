
from visual import *
from visual.controls import *
import math


#Takes in date (month and year)
base_yr = 561. 
in_month = float(raw_input("Enter a month "))
mnth = in_month/12.

in_year = float(raw_input("Enter a year 'YYYY' ")) #Error checking mechanism needed
yr = in_year + mnth

new_yr = yr + base_yr #total number of earth years since alignment

#Define sun/planet size and color
sun = sphere(pos=(0,0,0), radius=3, color=color.yellow)

# Planets from largest to smallest
jupiter = sphere(radius=1.5,color=(.847,.620,.570))

saturn = sphere(radius = 1.25, color =(.878,.949,.989))

uranus = sphere(radius = 1, color =(0,.663,1))   

neptune = sphere(radius = .8, color =color.blue)

earth = sphere(radius=.5, color=(.408,.545,.769))

venus = sphere(radius = .4, color=color.red)

mars = sphere(radius = .3, color =color.orange)

mercury = sphere(radius=.2, color=(.750,.750,.750))

#Lists of planets, corresponding spacing, time for orbit
posfactor = [.24,1.88, .62,1.,11.86,29.46,84.01,164.8]
size = [0.3, 2.5, .8, 1.5, 5, 10, 19, 30]
planets = [mercury,mars,venus,earth,jupiter,saturn,uranus,neptune]

#Aggregate planets, time of orbit, relative spacing
planets = zip(planets, posfactor, size) 

#Passes through list, determines position, and displays each planet
for planet, posfactor, size in planets:
        rot_num = new_yr/posfactor
        new_theta = rot_num*2*pi
        planet.pos = (cos(new_theta)*(sun.radius+planet.radius+size), sin(new_theta)*(sun.radius+planet.radius+size), 0)


~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             
~                                                                                                                                             

