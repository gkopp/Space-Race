#!/usr/bin/env python

# This program takes a text file that contains position information on all of
# the planets for each date the user entered while running the GUI (generated 
# by main program orbit.py). It checks the accuracy of the first date that the
# user inputted in orbit.py by calculating what the rotational angle (in revs)
# should be at that date for every planet and then comparing those results to 
# what the rotational angle actually is at that date for each planet in the
# simulation. It returns success if every planet in the simulation is within 
# .00001 of a revolution to where it's calculated position should be.

import math
import sys

def usage(status=0):
    if status == 1:
        print '''
        Usage: To run test_orbit.py, you must have already run orbit.py
        and used the "advance the simulation" feature by picking a month,
        day, and year from the menus and then clicking the advance button.
        '''
    sys.exit(status)

# given two ints, determines the angle between them on the unit circle in revolutions
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
    
    return angle/(2*math.pi) # divide by 2pi to get number of revolutions



pos_data = [] # stores the x and y values of each planet at every date tested
dates = [] # stores the dates positions were recorded on in the text file

planet_num = 0
# Parse file into appropriate lists
with open("planet_pos.txt", 'r') as fs: # open text file containing planet position information

    for line in fs:
        line =  line.strip().split()
 
        # Parse out date and convert day/month/year into a year value that accounts for days/months
        if line and line[0] == 'Planet': 
            date = line[4].split('/')

            month = float(date[0])/12 # convert month to years
            day = float(date[1])/365  # convert day to years
            year = float(date[2])
            base_year = 561 # the last recorded date all planets were aligned was 561 BC

            earth_revs = month + day + year + base_year # add base year so planets come from common starting place
          
            dates.append(earth_revs) # add to list holding the year values for each data sample

        # Parse out x and y positions for each planet
        elif line and line[0] != 'Planet' and line[0] != 'RESULTS': # filter out headings
            if line[0] != '____________________________________':
                x = float(line[1][1:-1])
                y = float(line[2][:-1])
                pos_data.append((x,y)) # add each revolution angle to a list
                planet_num = planet_num + 1
                if planet_num == 8:
                    break

if len(pos_data) == 0: # List would only be empty if there was no position data in text file 
                       # meaning the user didn't previously run orbit.py with the advance feature
    usage(1)           # Alert user of this and exit program


base_trial = [] # stores the position (in revs) of the first set of planet positions in the file
base_trial = pos_data[0:8] # add first set of planet positions

rev_length = [.24, 1.88, .62, 1., 11.86, 29.46, 84.01, 164.8] # lengths of each planets revolution relative to earth
                                                              # source: http://space-facts.com/orbital-periods-planets/
planet_names = ['mercury','mars','venus','earth','jupiter','saturn','uranus','neptune']

for i in range(0,8): # loops through all 8 planets

    print "Testing " + planet_names[i] + "..."
    rot_num = earth_revs/rev_length[i]    # find number of rotations planet made in given # of earth years
    calculated_theta = rot_num*2*math.pi  # convert to radians
    calculated_x = math.cos(calculated_theta) # given that angle, find corresponding x and y values
    calculated_y = math.sin(calculated_theta)

    # It's convenient to recalculate the angle to account for "overflow"
    calculated_angle = central_angle(calculated_x, calculated_y) # call function to convert theoretical x and y values into angle
    actual_angle =  central_angle(base_trial[i][0],base_trial[i][1]) # call same function on positions given in file

    # check if results are within .00001 revolutions of eachother
    if actual_angle >= calculated_angle - .00001 and actual_angle <= calculated_angle + .00001:
        continue
    else:
        print "ERROR: " + planet_names[i] + "'s does not match."

        usage # exit if results are not within .00001 revolutions

