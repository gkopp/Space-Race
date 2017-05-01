#Patricia Portmann, lab 6
#A code in python that uses the average distance from the sun
#to calculate speed

import math #math library for sqrt

plMass = input('Enter planet mass in kg: ')
#planet mass didn't end up mattering in the equation
distanceSun = input('Enter average distance from the sun in m: ')

# use 1/2m2v^2 = Gm1m2/r^2 to solve for v
# planet mass doesn't end up mattering

G = float(6.67 * pow(10, -11))#gravity constant
print('G is: {0}'.format(G))

sunMass = float(2.0 * pow(10,30))#mass of sun in kg
print('sunMass is: {0}'.format(sunMass))


square = float(math.sqrt(2*G*sunMass))

speed = float(square/distanceSun)

print('speed is {0}'.format(speed))
