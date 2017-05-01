#Provides user with the time (in years) for a chosen planet's complete orbit around the sun

x = str(raw_input("Enter a planet name: "))

print "In years on Earth: "

if x== "Mercury":
        period = (.75)
        print "%.2f "%  period
elif x == "Venus":
        period = 7./12.
        print "%.2f "%  period
elif x == "Earth":
        period = 1.
        print "%.2f "%  period
elif x == "Mars":
        period = 23./12.
        print "%.2f "%  period
elif x == "Jupiter":
        period = (142./12.)
        print "%.2f "% period
elif x == "Saturn":
        period = 354./12.
        print "%.2f "% period
elif x == "Uranus":
        period = 1009./12.
        print "%.2f "% period
elif x == "Neptune":
        period = 1979./12.
        print "%.2f "% period
else:
        print "Incorrect entry"
