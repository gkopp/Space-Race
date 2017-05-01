#!/usr/bin/env python

from visual.controls import *

# functions called on user driven events

def zoom(value): # called on button up events
    ball.radius = ball.radius * value

def toggle_ball_color(): # called on toggle switch flips
    if switch_color.value:
        ball.color = (.137,.247,.435)
    else:
        ball.color = (.820,.682,.133)



# create display window
display(x=350, y=0, width=350, height=350, range=1.5, forward=-vector(0,1,1), newzoom=1)

# initialize ball
ball = sphere(color=(.820,.682,.133), radius = 1)

# initialize control window
c = controls(x=0, y=0, width=350, height=350, range=60)

# create zoom out button
button_out = button(pos=(-30,-23), height=30, width=30, text='Zoom Out',
    action=lambda: zoom(.95))

# create zoom in button
button_in = button(pos=(-30,23), height=30, width=30, text='Zoom In',
    action=lambda: zoom(1.05))

# create color toggle
switch_color = toggle(pos=(30,0), width=10, height=10, text0='Gold',
    text1='Navy', action=lambda: toggle_ball_color())
