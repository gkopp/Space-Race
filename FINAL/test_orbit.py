#!/usr/bin/env python

# This program takes a text file that contains position information on all of
# the planets for each date the user entered while running the GUI (generated 
# by main program orbit.py)

import math

def central_angle(x , y):

    update_angle = 0
     
    if x > 0 and y >= 0:             # 1st quadrant
        update_angle = 0        

    if x <= 0 and y > 0:             # 2nd quadrant
        update_angle = math.pi/2

    if x < 0 and y <= 0:             # 3rd quadrant
    	  update_angle =  math.pi

    if x >= 0 and y < 0:             # 4th quadrant
        update_angle = 3*math.pi/2

    x = math.fabs(float(x))
    y = math.fabs(float(y))

    if (y == 0 or x == 0):
        angle = update_angle
    else:
        angle = math.atan(x/y) + update_angle
     
    return angle/(2*math.pi)

data = []
dates = []

planet_names = ['mercury','mars','venus','earth','jupiter','saturn','uranus','neptune']

# source: http://space-facts.com/orbital-periods-planets/
revolutions_per_year = [.24, 1.88, .62, 1., 11.86, 29.46, 84.01, 164.8] 

# Parse file into list of tuples with x and y coordinates
with open("planet_pos.txt", 'r') as fs:
    for line in fs:
        line =  line.strip().split()
 
        if line and line[0] == 'Planet': 
        	  date = line[4].split('/')
        	  year = float(date[0])/12 + float(date[1])/365 + float(date[2])
        	  dates.append(year)

        elif line and line[0] != 'Planet' and line[0] != 'RESULTS':
            if line[0] != '____________________________________':
                x = line[1][1:-1]
                y = line[2][:-1]
                angle = central_angle(x, y)
                data.append(angle)

print dates
trials = []

for i in xrange(0,len(data),8):
	 temp_list = data[i:i+8]
	 trials.append(temp_list)

for i in xrange(1,len(trials)):
	  earth_years = dates[i] - dates[0]
	  info = zip(revolutions_per_year, trials[0],trials[i])
	  for rev_frac, base_angle, curr_angle in info:
	  	  calculated_new_angle = (base_angle + rev_frac*earth_years*2*math.pi) % 1 
	  	  print calculated_new_angle
	  	  print curr_angle
	  print earth_years

#print trials[0]
#print trials[1]

