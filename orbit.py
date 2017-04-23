#!/usr/bin/env python
from __future__ import division, print_function
from visual import *
from visual.controls import *
import wx


################## FUNCTIONS THAT ARE CALLED ON EVENTS ###############

def togglecubecolor(evt): 
    choice = t1.GetSelection()
    #if choice == 0: # upper radio button (choice = 0)
    #    print "yp" #cube.color = color.red
    #else: # lower radio button (choice = 1)
    #    break  #cube.color = color.cyan

################ CREATE MAIN WINDOW AND DISPLAY WIDGET ################

w = window(title='Solar System',width=1200, height=720,
    x=0, y=0)

solar_system = display(window=w, x=20, y=20, width=650, height=650,
    forward=-vector(0,-3,1))

######################## ADD USER EVENT OBJECTS #######################

event_panel = w.panel

# toggle button for two viewing mode
t1 = wx.RadioBox(event_panel, pos=(800,100), size=(160, 60),
    choices = ['Interactive mode', 'Simulation mode'], style=wx.RA_SPECIFY_ROWS)
t1.Bind(wx.EVT_RADIOBOX, togglecubecolor)

# menu for year
years = []
for year in range(1900, 2500):
    years.append(str(year))
year_menu = wx.Choice(event_panel, choices=years, pos=(800,160))

# menu for month
months = []
for month in range(1,13):
    months.append(str(month))
month_menu = wx.Choice(event_panel, choices=months, pos=(800,260))

# menu for day
days = []
for day in range(1,32):
    days.append(str(day))
day_menu = wx.Choice(event_panel, choices=days, pos=(800,360))

######################## IMPLEMENT 3D ANIMATION #########################

# Define Sun/Planet attributes
sun = sphere(pos=(0,0,0), radius=3, color=color.yellow)

# Planets from largest to smallest
jupiter = sphere(radius=1.5,color=(.847,.620,.570))
jupiter.pos = (sun.radius+jupiter.radius+5, sun.radius+jupiter.radius+5,0)

saturn = sphere(radius = 1.25, color =(.878,.949,.989))
saturn.pos = (sun.radius+saturn.radius+10,sun.radius+saturn.radius+10,0)
uranus = sphere(radius = 1, color =(0,.663,1))
uranus.pos = (sun.radius+19+uranus.radius,sun.radius+uranus.radius+19,0)     

neptune = sphere(radius = .8, color =color.blue)
neptune.pos = (sun.radius+neptune.radius+30, sun.radius+neptune.radius+30,0)

earth = sphere(radius=.5, color=(.408,.545,.769))
earth.pos = (sun.radius+earth.radius+1.5,sun.radius+earth.radius+1.5,0)

venus = sphere(radius = .4, color=color.red)
venus.pos = (sun.radius+venus.radius+.8,sun.radius+venus.radius+.8,0)

mars = sphere(radius = .3, color =color.orange)
mars.pos = (sun.radius+mars.radius+2.5,sun.radius+mars.radius+2.5,0)

mercury = sphere(radius=.2, color=(.750,.750,.750))
mercury.pos = (sun.radius+mercury.radius+0.3,sun.radius+mercury.radius+0.3,0)

#control_panel = controls(x=0, y=0, width=700, height=700)
#year = menu(pos=(-70,70,0), height=7, width=25, text='Year')

# After creating the menu heading, add menu items:
#for num in range(1900, 2500):
#    year.items.append((str(num), None))

# create lists of planets and corresponding relative speeds
speeds = [1,.39, .24,.13,.02,.008,.003,.001]
planets = [mercury,mars,venus,earth,jupiter,saturn,uranus,neptune]

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
