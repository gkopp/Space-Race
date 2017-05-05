Data Structures Final Project
=============================

Members
-------

- Grace Kopp        (gkopp@nd.edu)
- Marya Poterek     (mpoterek@nd.edu)
- Patricia Portmann (pportman@nd.edu)

Summary
-------

This is the repository for our interactive solar system simulation program. We
created the program primarily using the vpython visual and wx libraries. Our
repository contains 2 directories: FINAL and individual_work. individual_work
contains programs that we worked on in the early stages of implementing our
project. These are the programs we used to learn how to use python, vpython, and
the physics of planetary motion. While none of these programs are called in any
form in our final project, we decided to include them in a separate directory
anyway because they were the building blocks of the final result. The FINAL
directory, then, is where our actual interactive solar system simulation final
product is. If the user runs orbit.py, the simulation will appear. This is
technically the only file needed to run the simulation. When running orbit.py,
whenever the user uses the "advance the simulation to a specified date
functionality," in addition to displaying the correct planet configuration in
the animation, the exact x and y coordinates that each planet advances too is
written to a text file along with the date that they were called for. This was
done to make our testing more precise. We then have a test program,
test_orbit.py, that reads in that file and parses the information. Then the
date corrsponding to the first set of data is used to determine what the planet
configuration should be on that date. This calculated position is compared to
the actual position to check accuracy. The test program is not super user
friendly because it was made for personal verification and not users.
