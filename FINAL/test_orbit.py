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



data = [] # stores the revolution number corresponsing to each planets position
dates = [] # stores the dates positions were recorded on in the text file

# source: http://space-facts.com/orbital-periods-planets/
# the number of revolutions each planet makes while earth makes one
revolutions_per_year = [.24, 1.88, .62, 1., 11.86, 29.46, 84.01, 164.8] 

# Parse file into appropriate lists
with open("planet_pos.txt", 'r') as fs: # open text file containing planet position information

    for line in fs:
        line =  line.strip().split()
 
        # Parse out date and convert day/month/year into a year value that accounts for days/months
        if line and line[0] == 'Planet': 
        	  date = line[4].split('/')
        	  year = float(date[0])/12 + float(date[1])/365 + float(date[2])
        	  dates.append(year) # add to list holding the year values for each data sample

        # Parse out x and y positions for each planet
        elif line and line[0] != 'Planet' and line[0] != 'RESULTS': # filter out headings
            if line[0] != '____________________________________':
                x = line[1][1:-1]
                y = line[2][:-1]
                angle = central_angle(x, y) # call function to convert x and y to # of revolutions
                data.append(angle) # add each revolution angle to a list

base_trial = [] # stores the position (in revs) of the first set of planet positions in the file
base_trial = data[0:8]

update_trial = [] # stores the position (in revs) of the second set of planet positions in the file
update_trial = data[8:18]

elapsed_time = dates[1] - dates[0] # time (in years) between data sets

calculated_position = []
for i in range(0,8):
    calculated_position.append((base_trial[i] + elapsed_time/revolutions_per_year[i])%1)

planet_names = ['mercury','mars','venus','earth','jupiter','saturn','uranus','neptune']

for i in range(0,8):
    print "Testing " + planet_names[i] + "..."
    if update_trial[i] >= calculated_position[i] - .2 and update_trial[i] <= (calculated_position[i] + .2)%1:
       continue
    else:
       print planet_names[i] + " test failed!"
       print update_trial[i] 
       print calculated_position[i]
