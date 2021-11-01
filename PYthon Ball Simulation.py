#Author: @sachieko
#
#Student ID: Redacted
#
#Purpose: To give output to a user at points in time detailing the velocity
#and height of a ball, and graphically display it in quickdraw.
#
#Program Name: Python - Ball Simulation.
#Version: 1.1
#
#Extra Program Notes: The balls time is output every 0.05 seconds and calculated
#for periods of 0.05 seconds originally instead of 0.1 seconds for accuracy and a smoother
#graphical output. This time can be changed, but a time lapse of 0.01 runs slower.
#

#
#Import sys function and the time function.
#This allows sleep function on time and the ability for system error statements
#
import sys
import time


#
#Equation for height:
#
#height = acceleration * time + .5 * acceleration * time * time
#
#Equation for Final Velocity
#
# veloc_final = initial_veloc + acceleration * time
#
#Equation for distance
# distance = velocity * time
#



#        STYLISTIC ADDITION
# 
# Prompt user for input. 1 = No Vertical Velocity  2 = With Vertical Velocity
#
# I added this feature so both versions of the ball could be seen, just for preference. 
#

sys.stderr.write('Welcome to the program.\n Enter \'1\' for no vertical velocity or \'2\' for with vertical velocity: ')

user_input = input()




#        ~ VARIABLES FOR CALCULATIONS ~ VARIABLES ARE HERE
#                       VARIABLES
#                        -------
#        
#
#Starting variable positions.
#
#vel for velocity    h for height     acc for acceleration
#
#delta_t = change in time. This will change how fast the program updates.
#
# Higher values of delta_t will cause the graphical display to be smoother, 
# but will cause the program to run slower.
#

ball_time = 0.00
ball_vel = 00.00
ball_h = 2.00
ball_acc = 9.81
delta_t = 0.05

#
#Horizontal Velocity of the ball and horizontal starting position
# 
# ball_horz = starting horizontal position, it starts centered, at 360pixels (-40 for radius of 40)
# delta_d is change in horizontal distance. Originally set at 5cm or 10 pixels per .05 seconds.
# delta_d is HORIZONTAL VELOCITY, it has no effect on how fast the ball falls.
#

ball_horz = 360
delta_d = 10



# GRAPHICAL OUTPUT
#Print the starting ball, named the_ball.
#           SCALE  1 pixel = .5 cm  OR 2 pixels = 1 centimetre
#          radius of 40, which is 20cm
#
print "circle",ball_horz+40,"140 40 the_ball"

sys.stdout.flush()


# GRAPHICAL OUTPUT
#starting Draw height will convert the ball height in the program to an output in pixels for #quickdraw. The starting draw height is 100 pixels, or 400 pixels above the ground.
#
draw_height = 500 - (ball_h * 100 * 200)

#
#                           END OF VARIABLES
#
#                            ----------
#
#         ~ END OF VARIABLES TO BE CHANGED ~ CHANGING VARIABLES PAST THIS POINT IS UNDESIREABLE

#
# Stage 2 ONLY : with vertical velocity.
#
if user_input == 1:
 while True: 
   #
   #If height is negative, print zero height by default.
   if ball_h < 0.00:
    #                     PHYSICS OUTPUT
    #Print current variables. Update graphical position.
     sys.stderr.write("Time:%3.2f s    Height:0.00 m  Velocity:%2.2f m/s\n" % (ball_time, ball_vel))

   else:
    #                     PHYSICS OUTPUT
    #Print current variables. Update graphical position of the ball.
     sys.stderr.write("Time:%3.2f s    Height:%1.2f m  Velocity:%2.2f m/s\n" % (ball_time, ball_h, ball_vel))
  
   #
   #Print the move command for the_ball
   print "move",ball_horz,draw_height,"the_ball"

   #                               /                Change in height                       \
   #Compute new height = height - (initial_velocity * DELTA TIME + ACC * DELTA TIME ** 2 *.5)
   ball_h = ball_h - (ball_vel * delta_t + ball_acc * 0.5 * (delta_t ** 2))
   # 
   #Compute the new velocity = velocity + ACC * DELTA TIME
   ball_vel = ball_vel + ball_acc * delta_t
 
   #
   #Compute the new time = time + 0.1s
   ball_time = ball_time + delta_t

   #        GRAPHICAL CALCULATIONS
   #Compute the new draw_height
   #Draw height will be calculated into pixels by the following.
   #
   #    draw_height =    500 - (ball_h * 100) * 2 
   #
   draw_height = 500 - (ball_h * 100) * 2

   #
   # check to change the gravity acceleration working against or with the ball.
   if ball_h <= 0.00:
     ball_vel = ball_vel * -1.00
   

   sys.stdout.flush()
   time.sleep(0.05)
   #
   # End of stage 2

#
# Stage 3 FULL VERSION with vertical velocity.
#

if user_input == 2:
 while True: 
   #
   #If height is negative, print zero height by default.
   if ball_h < 0.00:
    #
    #                     PHYSICS OUTPUT
    #Print current variables. Update graphical position.
     sys.stderr.write("Time:%3.2f s    Height:0.00 m  Velocity:%2.2f m/s\n" % (ball_time, ball_vel))

   else:
    #                     PHYSICS OUTPUT
    #Print current variables. Update graphical position of the ball.
     sys.stderr.write("Time:%3.2f s    Height:%1.2f m  Velocity:%2.2f m/s\n" % (ball_time, ball_h, ball_vel))
  
   #
   #Print the move command for the_ball
   print "move",ball_horz,draw_height,"the_ball"

   #                               /                Change in height                       \
   #Compute new height = height - (initial_velocity * DELTA TIME + ACC * DELTA TIME ** 2 *.5)
   ball_h = ball_h - (ball_vel * delta_t + ball_acc * 0.5 * (delta_t ** 2))
   # 
   #Compute the new velocity = velocity + ACC * DELTA TIME
   ball_vel = ball_vel + ball_acc * delta_t
 
   #
   #Compute the new time = time + 0.1s
   ball_time = ball_time + delta_t

   #        GRAPHICAL CALCULATIONS
   #Compute the new draw_height
   #Draw height will be calculated into pixels by the following.
   #
   #    draw_height =    500 - (ball_h * 100) * 2 
   #
   ball_horz = ball_horz + delta_d
   draw_height = 500 - (ball_h * 100) * 2

   #
   # check to change the gravity acceleration working against or with the ball.
   if ball_h <= 0.00:
     ball_vel = ball_vel * -1.00
   
   # check to see if the_ball hits the wall.
   if ball_horz >= 720 or ball_horz <= 0:
     delta_d = delta_d * -1
    
   sys.stdout.flush()
   time.sleep(0.05)
   #
   # End of stage 3
