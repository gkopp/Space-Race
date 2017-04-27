#!/usr/bin/env python

from __future__ import division, print_function
from visual import *
from visual.controls import *
import wx
import math

################## FUNCTIONS THAT ARE CALLED ON EVENTS ###############

def toggle_trail(evt): # turn trail on or off based on radio button

    choice = trail_toggle.GetSelection()
    planets = [mercury,mars,venus,earth,jupiter,saturn,uranus,neptune]
    if choice == 0: # top radio button
        for planet in planets:
            planet.trail.visible = True
    else: # bottom radio button
        for planet in planets:
            planet.trail.visible = False

def change_view(evt): # update the viewing angle based on slider

    y_value = view_angle.GetValue()
    solar_system.forward =-vector(0, y_value ,1)

def advance_simulation(evt): # move planets to configuration at date specified in menus

    base_yr = 561.     # year where we know the configuration of the planets

    day = day_menu.GetSelection() # get entered day from day menu
    if day == 0:                  # don't use "Day" menu label as legitimate date
        return
    day = day/365                 # convert to fraction of an Earth year

    month = month_menu.GetSelection() # get selected month from month menu
    if month == 0:                    # don't use "Month" menu label as legitimate date
        return
    month = month/12                  # convert to fraction of an Earth year

    year = year_menu.GetSelection()   # get selected year from year menu
    if year == 0:                     # don't use "Year" menu label as legitimate date
        return

    year = year + 1899 + base_yr + month + day # total number of years since base year

    #Lists of planets, corresponding spacing, time for orbit
    posfactor = [.24,1.88, .62,1.,11.86,29.46,84.01,164.8]
    size = [1.75, 2.6, 3.75, 4.75, 9, 16, 28.5, 43.75]
    planets = [mercury,mars,venus,earth,jupiter,saturn,uranus,neptune]

    #Aggregate planets, time of orbit, relative spacing
    planets = zip(planets, posfactor, size)

    #Passes through list, determines position, and displays each planet
    for planet, posfactor, size in planets:
        rot_num = year/posfactor
        new_theta = rot_num*2*pi
        planet.pos = (cos(new_theta)*(sun.radius+planet.radius+size), 
            sin(new_theta)*(sun.radius+planet.radius+size), 0)

    mars.speed = 0            # stop simulation
    speed_slider.SetValue = 0 # update slider


def run_simulation(evt): # update token speed value to default to run simulation
    mars.speed = 0.01 

def stop_simulation(evt): #update token speed value to 0 to stop simulation
    mars.speed = 0

def update_speed(evt):    # update token speed value to current slider value
    mars.speed = speed_slider.GetValue()*0.01

def update_zoom(evt):     # set window range to the current slider value
    solar_system.range = zoom_slider.GetValue()

################ CREATE MAIN WINDOW AND DISPLAY WIDGET ################

w = window(title='Solar System',width=1020, height=720,
    x=0, y=0)

solar_system = display(window=w, x=20, y=20, width=650, height=650,
    forward=-vector(0,0,1))

solar_system.autoscale = False
solar_system.range = 50          # set starting zoom of window 

######################## ADD USER EVENT OBJECTS #######################

event_panel = w.panel   # holds all of the controls

# toggle button for two viewing mode
trail_toggle = wx.RadioBox(event_panel, pos=(760,430), size=(160, 60),
    choices = ['Show trail', 'Hide trail'], style=wx.RA_SPECIFY_ROWS)
trail_toggle.Bind(wx.EVT_RADIOBOX, toggle_trail)

# title for checkboxes
wx.StaticText(event_panel, pos=(700,490), size=(300,30),
    label='Planets included in simulation:',
    style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

# planet check boxes for visibility
mercury_check = wx.CheckBox(event_panel, pos=(800,490), size=(160, 60),
    label = 'Mercury')
#mercury_check.Bind(wx.EVT_CHECKBOX, toggle_trail)

venus_check = wx.CheckBox(event_panel, pos=(800,510), size=(160, 60),
    label = 'Venus', style=wx.RA_SPECIFY_ROWS)

earth_check = wx.CheckBox(event_panel, pos=(800,530), size=(160, 60),
    label = 'Earth', style=wx.RA_SPECIFY_ROWS)

mars_check = wx.CheckBox(event_panel, pos=(800,550), size=(160, 60),
    label = 'Mars', style=wx.RA_SPECIFY_ROWS)

jupiter_check = wx.CheckBox(event_panel, pos=(800,570), size=(160, 60),
    label = 'Jupiter', style=wx.RA_SPECIFY_ROWS)

saturn_check = wx.CheckBox(event_panel, pos=(800,590), size=(160, 60),
    label = 'Saturn', style=wx.RA_SPECIFY_ROWS)

uranus_check = wx.CheckBox(event_panel, pos=(800,610), size=(160, 60),
    label = 'Uranus', style=wx.RA_SPECIFY_ROWS)

neptune_check = wx.CheckBox(event_panel, pos=(800,630), size=(160, 60),
    label = 'Neptune', style=wx.RA_SPECIFY_ROWS)

# date menus title
wx.StaticText(event_panel, pos=(690,130), size=(300,30),
    label='Advance simulation to specified date:',
    style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

# menu for year
years = []
years.append("Year")
for year in range(1900, 2500):
    years.append(str(year))
year_menu = wx.Choice(event_panel, choices=years, pos=(910,160))

# menu for month
months = ["      Month", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
month_menu = wx.Choice(event_panel, choices=months, pos=(690,160))

# menu for day
days = []
days.append("Day")
for day in range(1,32):
    days.append(str(day))
day_menu = wx.Choice(event_panel, choices=days, pos=(812,160))

# advance simulation button
advance =  wx.Button(event_panel, label='Advance', pos=(800,190))
advance.Bind(wx.EVT_BUTTON, advance_simulation)

# run simulation button
run_button = wx.Button(event_panel, label='Run', pos=(725,50))
run_button.Bind(wx.EVT_BUTTON, run_simulation)

# stop simulation button
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

# zoom slider title
wx.StaticText(event_panel, pos=(700,310), size=(300,30),
    label='Adjust zoom:',
    style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

# slider for zoom adjustment
zoom_slider = wx.Slider(event_panel, pos=(700,330), size=(300,20),
    minValue=5, maxValue=85)
zoom_slider.Bind(wx.EVT_SCROLL, update_zoom)

# speed slider title
wx.StaticText(event_panel, pos=(700,380), size=(300,30),
    label='Update simulation speed:',
    style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

# slider for speed adjustment
speed_slider = wx.Slider(event_panel, pos=(700,400), size=(300,20), minValue=.1,
    maxValue=10)
speed_slider.Bind(wx.EVT_SCROLL, update_speed)

######################## IMPLEMENT 3D ANIMATION #########################

# Define Sun/Planet attributes
sun = sphere(pos=(0,0,0), radius=3, color=color.yellow)
sun.visible = False

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
    planet.trail.visible = False
    planet.speed = 0.01

# draw trails

iterations = 0
for planet in planets:
    planet.visible = False

while(iterations < 102):
    rate(100)
    theta = 0.01*2*pi
    for planet in planets:
        planet.pos = rotate(planet.pos, 1*theta)
        planet.trail.append(pos=planet.pos)
    iterations = iterations + 1

for planet in planets:
    planet.visible = True
    planet.trail.visible = True

sun.visible = True

# perform animation

planets = zip(planets, speeds) # aggregate planet names and speeds

while(1):
    rate(100)         # max of 100 frames/second
    theta = mars.speed*2*pi
    iterations = iterations + 1
    for planet, speed in planets:
        planet.pos = rotate(planet.pos, speed*theta)
