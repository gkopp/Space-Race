#!/usr/bin/env python

from __future__ import division, print_function
from visual import *
from visual.controls import *
import wx
import math

######################### GLOBAL VARIABLES ###########################

advance = True

################## FUNCTIONS THAT ARE CALLED ON EVENTS ###############

def toggle_trail(evt): 
    choice = trail_toggle.GetSelection()
    planets = [mercury,mars,venus,earth,jupiter,saturn,uranus,neptune]
    if choice == 0: # top radio button
        for planet in planets:
            planet.trail.visible = True
    else: # bottom radio button
        for planet in planets:
            planet.trail.visible = False

def change_view(evt):
    y_value = view_angle.GetValue()
    solar_system.forward =-vector(0, y_value ,1)

def advance_simulation(evt):
    base_yr = 561.
    month = month_menu.GetSelection() 
    month = month/12
    year = year_menu.GetSelection()
    year = year + base_yr

    #Lists of planets, corresponding spacing, time for orbit
    posfactor = [.24,1.88, .62,1.,11.86,29.46,84.01,164.8]
    size = [0.3, 2.5, .8, 1.5, 5, 10, 19, 30]
    planets = [mercury,mars,venus,earth,jupiter,saturn,uranus,neptune]

    #Aggregate planets, time of orbit, relative spacing
    planets = zip(planets, posfactor, size)

    #Passes through list, determines position, and displays each planet
    for planet, posfactor, size in planets:
        rot_num = year/posfactor
        new_theta = rot_num*2*pi
        planet.pos = (cos(new_theta)*(sun.radius+planet.radius+size), 
            sin(new_theta)*(sun.radius+planet.radius+size), 0)
        planet.trail.visible = False
    mars.speed = 0

def run_simulation(evt):
    mars.speed = 0.01 

def stop_simulation(evt):
    mars.speed = 0

#def update_speed(evt):
#    adjust_speed = speed_slider.GetValue()

################ CREATE MAIN WINDOW AND DISPLAY WIDGET ################

w = window(title='Solar System',width=1020, height=720,
    x=0, y=0)

solar_system = display(window=w, x=20, y=20, width=650, height=650,
    forward=-vector(0,0,1))

######################## ADD USER EVENT OBJECTS #######################

event_panel = w.panel

# toggle button for two viewing mode
trail_toggle = wx.RadioBox(event_panel, pos=(760,300), size=(160, 60),
    choices = ['Show trail', 'Hide trail'], style=wx.RA_SPECIFY_ROWS)
trail_toggle.Bind(wx.EVT_RADIOBOX, toggle_trail)


# date menus title
wx.StaticText(event_panel, pos=(690,130), size=(300,30),
    label='Advance simulation to specified date:',
    style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

# menu for year
years = []
years.append("Year")
for year in range(1900, 2500):
    years.append(str(year))
year_menu = wx.Choice(event_panel, choices=years, pos=(700,160))

# menu for month
months = []
months.append("Month")
for month in range(1,13):
    months.append(str(month))
month_menu = wx.Choice(event_panel, choices=months, pos=(800,160))

# menu for day
days = []
days.append("Day")
for day in range(1,32):
    days.append(str(day))
day_menu = wx.Choice(event_panel, choices=days, pos=(910,160))
day_menu.Bind(wx.EVT_CHOICE, choose)

# advance simulation button
advance =  wx.Button(event_panel, label='Advance', pos=(800,190))
advance.Bind(wx.EVT_BUTTON, advance_simulation)

run_button = wx.Button(event_panel, label='Run', pos=(725,50))
run_button.Bind(wx.EVT_BUTTON, run_simulation)

stop_button = wx.Button(event_panel, label='Stop', pos=(860,50))
stop_button.Bind(wx.EVT_BUTTON, stop_simulation)

# angle update title
wx.StaticText(event_panel, pos=(700,240), size=(300,30),
    label='Update rotational viewing angle:',
    style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

# slider for view angle
view_angle = wx.Slider(event_panel, pos=(700,260), size=(300,20),
    minValue=-7, maxValue=0)
view_angle.Bind(wx.EVT_SCROLL, change_view)

# slider for speed adjustment
speed_slider = wx.Slider(event_panel, pos=(700,560), size=(300,20), minValue=.1, maxValue=10)
#speed_slider.Bind(wx.EVT_SCROLL, update_speed)

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



# create lists of planets and corresponding relative speeds
speeds = [1,.39, .24,.13,.02,.008,.003,.001]
planets = [mercury,mars,venus,earth,jupiter,saturn,uranus,neptune]

# initialize trail for each planet
for planet in planets:
    planet.trail = curve(color = color.white)
    planet.speed = 0.01
    planet.make_trail=False

planets = zip(planets, speeds) # aggregate planet names and speeds

dt = 0.01

# perform animation

iterations = 0
advance = True
dt = 0.01

while(1):
    rate(100)         # max of 100 frames/second
    theta = mars.speed*2*pi
    iterations = iterations + 1
    for planet, speed in planets:
        planet.pos = rotate(planet.pos, speed*theta)
        if iterations*speed*theta < 25 and mars.speed != 0:
            planet.trail.append(pos=planet.pos)

