import math

#Walker-Delta

#Author:        DSE-S12
#Affiliation:   Delft University of Technology

#INPUTS
# res          = Resolution [km/pixel].
# pixel_width  = Number of pixels in the width axis [pixels].
# pixel_height = Number of pixels in the height axis [pixels].
# alt          = Orbital altitude.
# field_view   = Field of view [rad].

#VARIABLES
# d_omega      = Nodal spacing interval between planes [rad].
# d_nu         = In-plane phasing interval btw. satellites [rad].
# Re           = Earth Radius [km]

#OUTPUTS
# inc          = Inclination [rad].
# s            = Number of satellites per orbital plane.
# T            = Total number of satellites.
# P            = Number of orbital planes.


Re = 6371
alt = 500

res = 0.5
pixel_width = 1000
pixel_height = 1000
width = res*pixel_width
height = res*pixel_height


width = 2*alt*math.tan(40*math.pi/180)
print(width)
height = 2*alt*math.tan(17*math.pi/180)
number_of_images = 1

#Find inclination
inc = math.pi/2-2*math.pi/(2*math.pi*Re)*(width/2*number_of_images)

print("Inclination [deg]: ",inc*180/math.pi)

#Find number of orbital planes

#If height<=width
node_width = 2*(width/2)*math.sin(inc)
P = 2*math.pi*Re/node_width
print(P)
node_height = height
print(height)
s = 2*math.pi*Re/node_height
print(s)




