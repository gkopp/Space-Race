#!/usr/bin/env python

# This program takes a text file that contains position information on all of
# the planets for each date the user entered while running the GUI (generated 
# by main program orbit.py)

import math

# Given a x and y coordinate, program returns number of revolution number that corresponds to that
# point (where once around the unit circle is one revolution)

def central_angle(x , y):
    x = float(x)
    y = float(y)
   
    if x > 0 and y >= 0:             # 1st quadrant
        update_angle = 0        

    if x <= 0 and y > 0:             # 2nd quadrant
        update_angle = math.pi/2

    if x < 0 and y <= 0:             # 3rd quadrant
    	  update_angle =  math.pi

    if x >= 0 and y < 0:             # 4th quadrant
        update_angle = 3*math.pi/2

    # take absolute value of numbers
    x = math.fabs(x)
    y = math.fabs(y)

    if (y == 0 or x == 0):
        angle = update_angle # avoids dividing by 0
    else:
        angle = math.atan(x/y) + update_angle 
    
    return angle/(2*math.pi)



pos_data = [] # stores the revolution number corresponsing to each planets position
dates = [] # stores the dates positions were recorded on in the text file

# Parse file into appropriate lists
with open("planet_pos.txt", 'r') as fs: # open text file containing planet position information

    for line in fs:
        line =  line.strip().split()
 
        # Parse out date and convert day/month/year into a year value that accounts for days/months
        if line and line[0] == 'Planet': 
            date = line[4].split('/')

            month = float(date[0])/12
            day = float(date[1])/365
            year = float(date[2])
            earth_revs = month + day + year + 561
          
            dates.append(earth_revs) # add to list holding the year values for each data sample

        # Parse out x and y positions for each planet
        elif line and line[0] != 'Planet' and line[0] != 'RESULTS': # filter out headings
            if line[0] != '____________________________________':
                x = float(line[1][1:-1])
                y = float(line[2][:-1])
                pos_data.append((x,y)) # add each revolution angle to a list

all_trial_data = []
for i in range(0,len(pos_data),8):
    temp_trial = []
    temp_trial = pos_data[i:i+8]
    print temp_trial
    all_trial_data.append(temp_trial)

base_trial = [] # stores the position (in revs) of the first set of planet positions in the file
base_trial = pos_data[0:8]

rev_length = [.24, 1.88, .62, 1., 11.86, 29.46, 84.01, 164.8] # lengths of each planets revolution relative to earth
                                                              # source: http://space-facts.com/orbital-periods-planets/

rot_num = earth_revs/.24
calculated_theta = rot_num*2*math.pi
calculated_x = math.cos(calculated_theta)
calculated_y = math.sin(calculated_theta)
print central_angle(calculated_x, calculated_y)
print central_angle(base_trial[0][0],base_trial[0][1])

