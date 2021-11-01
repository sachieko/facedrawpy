#Written in: Notepad
#Author: @sachieko

#Student ID: Redacted

#Date: January 28th, 2009

#Version: 1.2
#Name: FaceDraw 1.2
#Image is centered if 400 = x and 300 = y.
#Image is based off an existing "Smiley Face" which is loosely defined.
#Reason for Version Changes: Reordering of the face, structure changes.
#
#Purpose: To draw a face on the screen centered on coordinates determined by the user.
#


#

# Prompt for user input using System commands.

#


import sys



sys.stderr.write('Please enter an X coordinate(0-800): ')
x = input()



sys.stderr.write('Please enter a Y Coordinate (0-600): ')

y = input()



#

#Calculate the different calculations beforehand.

#eyes = -50 and +50 horizontal pixels. (x)

#No nose for this design.

#Smile = 100 width, arc of depth 25.

#Eyes will be filled arcs with a pupil.
#




eye_level = y-75
lefteye = x-125
righteye = x
+25
mouth_x = x-100

mouth_y = y-50
mouth_w = 200
mouth_h = 150
angle_s = 0
angle_f = -180





#

#Print the first layer.
#Face, eye outlines, mouth outline, white of the eyes
#Eye Arcs will be 100 pixels in width, 125 height, full 180 degree Arcfill.
#The Eye Arcs will form the outline for the white of the eyes, so I
#have shifted the values accordingly so they are not covered up by the actual eyes.
#

eye_width = 100
eye_height = 100



print "color 255 244 53"

print "fillcircle",x,y,150

print "color 0 0 0"
print "fillarc",lefteye-10,eye_level-10,eye_width+20,eye_height+40,0,179
print "fillarc",righteye-10,eye_level-10,eye_width+20,eye_height+40,0,179

#
#mouth arc
#This will form the outline for the mouth when it is drawn ontop.
#I have shifted the mouth values accordingly so it does not overlap the mouth.
#

print "color 0 0 0"
print "fillarc",mouth_x-10,mouth_y-20,mouth_w+25,mouth_h+30,angle_s,angle_f

#
#Print the white of the eyes
#this prints the eyes.
#
print "color 255 255 255"
print "fillarc",lefteye,eye_level,eye_width,eye_height,0,180
print "fillarc",righteye,eye_level,eye_width,eye_height,0,180


#

#Print the second layer. Pupils + Tongue + Mouth Opening
#
#Pupils will be located in the upper right, so shift them 75 pixels right, 15 down
#to get the pupils into a more aesthetic position.
#


print "color 0 0 0"
print "fillcircle",lefteye+75,eye_level+15,15
print "fillcircle",righteye+76,eye_level+15,15

#
#Mouth
#

print "color 160 40 40"
print "fillarc",mouth_x,mouth_y,mouth_w,mouth_h,angle_s,angle_f

#
#Print the final layer.
#
#The tongue and hair (hair done with a grid.)
#It will be a function of the previous mouth fill.
#and the arc will hit both edges of the mouth. The start angle turns out to 160 degrees.
#the end angle turns out to be exactly -145 degrees from the starting 160 degrees.
#

tongue_x = x-50
tongue_y = y+80
tongue_w = 100
tongue_h = 50

print "color 255 0 235"
print "fillarc",tongue_x,tongue_y,tongue_w,tongue_h-10,160,-145

#
#The hair as a grid.
#circle is 150 in radius, so -50 x pixels and -140 y pixels should be good for the hair patch.
#Number of divisions in the grid will be fairly high, 45 by 45 as an example.
#


hair_x = x-50
hair_y = y-170
hair_w = 100
hair_h = 60


print "color 130 100 60"
print "grid",hair_x,hair_y,hair_w,hair_h,45,45

#
#
# Print Output to User indicating the task is complete.
#
#


sys.stderr.write('FaceDraw has drawn the face in Quickdraw. Program End.')






