#!/usr/bin/env python

# Grace Kopp, Marya Poterek, and Patricia Portmann

# This program is a graphical user interface for an interactive solar
# system simulation. Using vpython and the wx widgets library, our GUI
# demonstrates the planets orbiting the sun with accurate relative sizes,
# distances from the sun, and speeds. The user can interact with this
# with sliders that update the zoom, angle of the view, and speed of the
# simulation. There's also a radio button giving the option to view or 
# hide the orbital paths, checkboxes allowing the user to choose which
# planets they want visible, run/stop/exit simulation buttons, and menus
# that the user can use to selct a month, day, and year, and then advance
# the simulation to that date.

from __future__ import division, print_function
from visual import *
from visual.controls import *
import wx
import math

################## FUNCTIONS THAT ARE CALLED ON EVENTS ##################


def leave(evt): # exit simulation when exit button selected
    exit()

def toggle_trail(evt): # turn trail on or off based on radio button
    choice = trail_toggle.GetSelection()
    planets = [mercury,mars,venus,earth,jupiter,saturn,uranus,neptune]
    if choice == 0: # top radio button
        for planet in planets:
            planet.trail.visible = False
    else: # bottom radio button
        for planet in planets:
            planet.trail.visible = True

def change_view(evt): # update the viewing angle based on slider
    y_value = view_angle.GetValue()
    solar_system.forward =-vector(0, y_value ,1)

def advance_simulation(evt): # move planets to configuration at date specified in menus

    base_yr = 561.     # year where we know the configuration of the planets
    
    # SOURCE: http://curious.astro.cornell.edu/about-us/57-our-solar-system/
    # planets-and-dwarf-planets/orbits/246-when-was-the-last-time-all-9-planets
    # -were-aligned-beginner

    # TL;DR: The planets were last aligned on 561 B.C. We arbitrarily put that alignment
    # at (1,0,0) for simplicity, but the only difference would be angle offset/ where the
    # x and y axises are defined

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
    saturns_ring.pos = saturn.pos
    mars.speed = 0            # stop simulation

def stop_simulation(evt): #update token speed value to 0 to stop simulation
    mars.speed = 0

def update_speed(evt):    # update token speed value to current slider value
    mars.speed = speed_slider.GetValue()*0.01

def update_zoom(evt):     # set window range to the current slider value
    solar_system.range = zoom_slider.GetValue()

# checkbox functions for each of the check boxes that turn on/off the visibility
# of specified planets (Originally was all in one function but program ran faster
# with a different event function for each planet checkbox)

def mercury_visible(evt):  
    if (mercury_check.GetValue() == False):
        mercury.visible = False
    else:
        mercury.visible = True

def venus_visible(evt):
    if (venus_check.GetValue() == False):
        venus.visible = False
    else:
        venus.visible = True

def earth_visible(evt):
    if (earth_check.GetValue() == False):
        earth.visible = False
    else:
        earth.visible = True

def mars_visible(evt):
    if (mars_check.GetValue() == False):
        mars.visible = False
    else:
        mars.visible = True

def jupiter_visible(evt):
    if (jupiter_check.GetValue() == False):
        jupiter.visible = False
    else:
        jupiter.visible = True

def saturn_visible(evt):
    if (saturn_check.GetValue() == False):
        saturn.visible = False
        saturns_ring.visible = False
    else:
        saturn.visible = True
        saturns_ring.visible = True

def uranus_visible(evt):
    if (uranus_check.GetValue() == False):
        uranus.visible = False
    else:
        uranus.visible = True 

def neptune_visible(evt):
    if (neptune_check.GetValue() == False):
        neptune.visible = False
    else:
        neptune.visible = True

################ CREATE MAIN WINDOW AND DISPLAY WIDGET ################

w = window(title='Interactive Solar System Simulation',width=1020, height=720,
    x=100, y=0)

solar_system = display(window=w, x=20, y=20, width=650, height=650,
    forward=-vector(0,-2,1))

solar_system.autoscale = False
solar_system.range = 50          # set starting zoom of window

######################## ADD USER EVENT OBJECTS #######################

event_panel = w.panel   # holds all of the controls

# toggle for trail visibility
trail_toggle = wx.RadioBox(event_panel, pos=(760,270), size=(160, 60),
    choices = ['Hide orbital path', 'Show orbital path'], style=wx.RA_SPECIFY_ROWS)
trail_toggle.Bind(wx.EVT_RADIOBOX, toggle_trail)

# title for checkboxes
wx.StaticText(event_panel, pos=(690,460), size=(300,30),
    label='Planets included in simulation:',
    style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

# planet check boxes for visibility
mercury_check = wx.CheckBox(event_panel, size=(160, 20),
    label = 'Mercury', style = wx.ALIGN_RIGHT, pos = (800,480))
mercury_check.SetValue(True)
mercury_check.Bind(wx.EVT_CHECKBOX, mercury_visible)

venus_check = wx.CheckBox(event_panel, pos=(800,500), size=(160, 20),
    label = 'Venus', style=wx.RA_SPECIFY_ROWS)
venus_check.SetValue(True)
venus_check.Bind(wx.EVT_CHECKBOX, venus_visible)

earth_check = wx.CheckBox(event_panel, pos=(800,520), size=(160, 20),
    label = 'Earth', style=wx.RA_SPECIFY_ROWS)
earth_check.SetValue(True)
earth_check.Bind(wx.EVT_CHECKBOX, earth_visible)

mars_check = wx.CheckBox(event_panel, pos=(800,540), size=(160, 20),
    label = 'Mars', style=wx.RA_SPECIFY_ROWS)
mars_check.SetValue(True)
mars_check.Bind(wx.EVT_CHECKBOX, mars_visible)

jupiter_check = wx.CheckBox(event_panel, pos=(800,560), size=(160, 20),
    label = 'Jupiter', style=wx.RA_SPECIFY_ROWS)
jupiter_check.SetValue(True)
jupiter_check.Bind(wx.EVT_CHECKBOX, jupiter_visible)

saturn_check = wx.CheckBox(event_panel, pos=(800,580), size=(160, 20),
    label = 'Saturn', style=wx.RA_SPECIFY_ROWS)
saturn_check.SetValue(True)
saturn_check.Bind(wx.EVT_CHECKBOX, saturn_visible)

uranus_check = wx.CheckBox(event_panel, pos=(800,600), size=(160, 20),
    label = 'Uranus', style=wx.RA_SPECIFY_ROWS)
uranus_check.SetValue(True)
uranus_check.Bind(wx.EVT_CHECKBOX, uranus_visible)

neptune_check = wx.CheckBox(event_panel, pos=(800,620), size=(160, 20),
    label = 'Neptune', style=wx.RA_SPECIFY_ROWS)
neptune_check.SetValue(True)
neptune_check.Bind(wx.EVT_CHECKBOX, neptune_visible)

# date menus title
wx.StaticText(event_panel, pos=(690,352), size=(300,30),
    label='Advance simulation to specified date:',
    style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

# menu for year
years = []
years.append("Year")
for year in range(1900, 2500):
    years.append(str(year))
year_menu = wx.Choice(event_panel, choices=years, pos=(910,380))

# menu for month
months = ["Month", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
month_menu = wx.Choice(event_panel, choices=months, pos=(690,380))

# menu for day
days = []
days.append("Day")
for day in range(1,32):
    days.append(str(day))
day_menu = wx.Choice(event_panel, choices=days, pos=(820,380))

# advance simulation button
advance =  wx.Button(event_panel, label='Advance', pos=(790,410))
advance.Bind(wx.EVT_BUTTON, advance_simulation)

# run simulation button
run_button = wx.Button(event_panel, label='Run', pos=(695,50))
run_button.Bind(wx.EVT_BUTTON, update_speed)

# stop simulation button
stop_button = wx.Button(event_panel, label='Stop', pos=(798,50))
stop_button.Bind(wx.EVT_BUTTON, stop_simulation)

exit_button = wx.Button(event_panel, label='Exit', pos=(900,50))
exit_button.Bind(wx.EVT_BUTTON, leave)

# angle update title
wx.StaticText(event_panel, pos=(700,160), size=(300,30),
    label='Update viewing angle:',
    style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

# slider for view angle
view_angle = wx.Slider(event_panel, pos=(700,180), size=(300,20),
    minValue=-7, maxValue=0, value = -2)
view_angle.Bind(wx.EVT_SCROLL, change_view)

# zoom slider title
wx.StaticText(event_panel, pos=(700,210), size=(300,30),
    label='Adjust zoom:',
    style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

# slider for zoom adjustment
zoom_slider = wx.Slider(event_panel, pos=(700,230), size=(300,20),
    minValue=5, maxValue=85, value = 50)
zoom_slider.Bind(wx.EVT_SCROLL, update_zoom)

# speed slider title
wx.StaticText(event_panel, pos=(700,105), size=(300,30),
    label='Update simulation speed:',
    style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

# slider for speed adjustment
speed_slider = wx.Slider(event_panel, pos=(700,130), size=(300,20), minValue=.1,
    maxValue=10, value = 1)
speed_slider.Bind(wx.EVT_SCROLL, update_speed)

########################## INITIALIZE PLANETS #############################

# Define Sun/Planet attributes
sun = sphere(pos=(0,0,0), radius=3, color=color.yellow, material=materials.emissive)
sun.visible = False

# Planets from largest to smallest
jupiter = sphere(radius=1.5,color=(.847,.620,.570))
jupiter.pos = (sun.radius+jupiter.radius+5, sun.radius+jupiter.radius+5,0)

saturn = sphere(radius = 1.25, color =(.878,.949,.989))
saturn.pos = (sun.radius+saturn.radius+10,sun.radius+saturn.radius+10,0)
saturns_ring = ring(axis=(1,1,4), radius=saturn.radius+1, thickness=0.25)
saturns_ring.pos = (sun.radius+saturn.radius+8,sun.radius+saturn.radius+11.5,0)
saturns_ring.color = color.cyan
saturns_ring.visible = False

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

############################# DRAW TRAILS #################################

# create lists of planets and corresponding relative speeds
speeds = [1,.39, .24,.13,.02,.008,.003,.001]
planets = [mercury,mars,venus,earth,jupiter,saturn,uranus,neptune]

# initialize trail for each planet
for planet in planets:
    planet.trail = curve(color = color.white)
    planet.trail.visible = False # keep invisible until full circle drawn
    planet.speed = 0.01

# draw trails

iterations = 0
for planet in planets:
    planet.visible = False # keep invisible until full circle drawn

while(iterations < 102):
    rate(100)
    theta = 0.01*2*pi
    for planet in planets:
        planet.pos = rotate(planet.pos, 1*theta)
        planet.trail.append(pos=planet.pos)
    iterations = iterations + 1
    
for planet in planets:
    planet.visible = True # make everything visible once trail loaded

sun.visible = True
saturns_ring.visible = True

####################### PERFORM ANIMATION ###########################

planets = zip(planets, speeds) # aggregate planet names and speeds

while(1):
    rate(100)  # max of 100 frames/second
    theta = mars.speed*2*pi
    iterations = iterations + 1
    for planet, speed in planets:
        planet.pos = rotate(planet.pos, speed*theta) # update each planet position
    saturns_ring.pos = rotate(saturns_ring.pos, .008*theta) # update saturns ring position

