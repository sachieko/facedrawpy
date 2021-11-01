#Quickdraw Graphing Tool
#Version 1.1
#Author: @sachieko
#ID: Null
#
#Purpose: To draw a line, circle, or parabola based on the input of the user.
#Mimic a graphing calculator in theory. This is done through a series of functions.
#Every function listed in the print command in the menu() function is a function.
#
#ALL PRINT COMMANDS WITH 'COLOR' ARE JUST DIFFERENT COLORS. No significant info is in a print command
#that contains the syntax 'color _ _ _" These numbers mean nothing to the program except whether
#the line is blue, red, green, or purple.
#
#Imported sys for system error commands to write commands to the user, and flush commands.
#imported time for the sleep function so the user can read when their input is typed wrong.
import sys
import time

#
#Screenwidth variables for calculating the functions.
#l = left side  r = right side.
#u is top   d is bottom
#Warning: This program cannot be used in full screen by changing these variables. Not fullscreenable.
#This is because the program does not calculate well for values past the edges of the screen.
#If I changed the conversion rates for calculating the center of the screen, this would work.
#However the program wouldn't work in the normal window size. There is probably a solution but it's beyond the scope of this program's needs
swidth_l = -20
swidth_r = 20
sheight_u = 20
sheight_d = -20
centerx = 400
centery = 300
#This variable is for the parabola increments. smaller values give you a smoother curve.
paraincrement = 0.1
#These are for the length of the ticks in the quickdraw program. Second is for placement of the text numbers.
ticklength = 5
ticklength2 = 7

#
#This function converts the input into capitals to avoid case sensitive errors.
def convertinput():
   global prompt
   prompt = prompt.upper()

#Main function. prompts for user input after using the axes function.
#This returns the prompt for the main program.
#This function also informs the user of the commands they can use.
def menu():
   global prompt
   sys.stderr.write( "\n===================================================================\n")
   sys.stderr.write( "\n||          ~ Welcome to Quickdraw Graphing Tool 1.1 ~           ||\n")
   sys.stderr.write( "\n||  [Graphing Functions]                  [Other Functions]      ||\n")
   sys.stderr.write( "\n||  Line   Circle   Point                  Clear    Exit         ||\n")
   sys.stderr.write( "\n||  Parabola  Cubic                     Convert a Fraction.      ||\n")
   sys.stderr.write( "\n||                    Author: @sachieko                          ||\n")
   sys.stderr.write( "\n===================================================================\n")
   sys.stderr.write( "\nNote: Please use the 'Convert' command to convert your fractions to decimals.")
   sys.stderr.write("\nCommands: Line, Circle, Parabola, Point, Cubic, Convert, Clear, Exit.")
   sys.stderr.write("\nPlease enter a command:")
   prompt = raw_input()
   convertinput()
   return prompt
  

#
#These functions converts x and y values into coordinates for the quickdraw program.
#
# 400,300 = 0,0    400,330 = 0,-1   400,270 = 0,1 
# 430,300 = 1,0   370,300 = -1,0    430,270 = 1,1  370,330 = -1,-1
# 
# Converting to quickdraw to X values
# 1 unit is 30 pixels by the following calculations.
#
# x*30 + 400 = result_x  y*-30 + 300 = result_y
#
# These return the x and y values in pixels for quickdraw.
def convert_x(x):
    result_x = x*30 + centerx
    return result_x

def convert_y(y):
    result_y = y*-30 + centery
    return result_y

#converts any number into pixels, used for radius.
#this returns the radius in pixels.
#30 pixels = 1 unit so multiply the value by 30.
def convert_r(r):
    result_r = r*30
    return result_r
   
   

#
#This is the plot_axes function, it makes a white background and then axes 
#on the top of the background.
#    600/20 = 30 pixels between points. -10 to 10 for vertical. 
#    800/30 = 26 units rounded down. so -13 to 13 for horizontal coordinates, 
#-14 to 14 covers the edges of the window though.
# This is also used for the function CLEAR if a user wishes to use it.
#
# The ticks for the axes are lines of 10 pixels in length. I used two seperate loops to cover each axis.
#Center of the screen is 400,300 pixels.
def plot_axes():
   global xcoord
   x_axis = swidth_l
   y_axis = sheight_u
   print "color 255 255 255"
   print "fillrect",convert_x(swidth_l),convert_y(sheight_u),convert_x(swidth_r),convert_y(sheight_d)
   print "color 0 0 0"
   print "line",convert_x(swidth_l),centery,convert_x(swidth_r),centery
   print "line",centerx,convert_y(sheight_u),centerx,convert_y(sheight_d)
   while x_axis < swidth_r: 
     x_axis = x_axis + 1
     x_line = convert_x(x_axis)
     print "line",x_line,(centery - ticklength),x_line,(centery + ticklength)
     print "text",x_axis,x_line,(centery - ticklength2)
   while y_axis >= sheight_d:
     y_line = convert_y(y_axis)
     print "line",(centerx - ticklength),y_line,(centerx + ticklength),y_line
     print "text",y_axis,(centerx + ticklength2),y_line
     y_axis = y_axis - 1
     sys.stdout.flush()
#
#The exit function, allows user to exit the program from the command prompt.
#Closes quickdraw and then the program prompt.
def exit1():
   print "quit"
   sys.stdout.flush()
#
   


#
#This function will perform the line function of the program.
#equation:  y = mx + b
#
#calculate the line at -14=x and 14=x and draw a line between those two points. 
def plot_line():
    sys.stderr.write("Equation of a line: y = mx + b\n m = slope, b = y intercept.\n")
    sys.stderr.write("Please enter the slope of the line: ")
    slope_m = input()
    sys.stderr.write("Please enter the y-intercept: ")
    y_cept = input()
    point_1 = slope_m * (swidth_l) + y_cept
    point_2 = slope_m * (swidth_r) + y_cept
    print "color 0 255 0"
    print "line",convert_x(swidth_l),convert_y(point_1),convert_x(swidth_r),convert_y(point_2)
    sys.stdout.flush()
    
# 
#This function will perform the circle function of the program.
#equation of a circle:  (x-a)^2+(y-b)^2 = r^2
#This function plots a circle centered on (a,b) with a radius of r. In pixels the radius is r*30
#This uses the convert function to find the center of the circle by passing values a and b.
#The radius is also converted using convert_r
#
def plot_circle():
   sys.stderr.write("Equation of a circle: (x-a)^2 + (y-b)^2 = r^2 \n a = x coordinate, b = y coordinate, r = radius.\n")
   sys.stderr.write("Please enter the x coordinate of the circle: ")
   coord_a = input()
   sys.stderr.write("Please enter the y coordinate of the circle: ")
   coord_b = input()
   sys.stderr.write("Please enter the radius of the circle: ")
   radius_r = input()
   print "color 0 0 255"
   print "circle",convert_x(coord_a),convert_y(coord_b),convert_r(radius_r)
   sys.stdout.flush()

#
#This function will perform the parabola function of the program.
#Equation used for the parabola = a(x-b)^2+c
#This must be done using probably hundreds or thousands of line commands..
#I will create a loop that draws from the left side of the screen to the right.
#Basically I'll create a loop to create a line segment, plot it, and then have to remember that plot and repeat with 
#the end point being the new beginning point and calculate the new endpoint beforehand, rinse and repeat.
#
#It will calculate every point on the parabola from -14 -> 14 at every 0.1 difference in value.
#
#In general, the loop will find y at y = (a(x-b)^2) + c and then print at the converted value for x and y.
#It starts at x= -14
#Then it will add 0.1 to the x value, and calculate an endline variable and calculate y at that x value.
#The endline variable becomes the new startline, and the endline is calculated at an addition +0.1 x value.
#
def plot_parabola():
   sys.stderr.write("Equation of a parabola: a(x-b)^2 + c \n a = horizontal stretch. b = x coordinate of vertex. c = y coordinate of vertex.\n")
   sys.stderr.write("Please enter the a value: ")
   horizontal_a = input()
   sys.stderr.write("Please enter the b value: ")
   coord_b = input()
   sys.stderr.write("Please enter the c value: ")
   coord_c = input()
   x_startline = swidth_l
   print "color 255 0 0"
   #This while loop will perform calculations for the line end points, plot, then repeat for all x values in the range.
   #It starts as -14.0 = x.  The y_startline and y_endline are calculated with the parabola equation.
   while x_startline <= swidth_r:
    y_startline = horizontal_a * (x_startline - coord_b) ** 2 + coord_c
    x_endline = x_startline + paraincrement
    y_endline = horizontal_a * (x_endline - coord_b) ** 2 + coord_c
    print "line",convert_x(x_startline),convert_y(y_startline),convert_x(x_endline),convert_y(y_endline)
    x_startline = x_startline + paraincrement
    x_endline = x_endline + paraincrement
    sys.stdout.flush()
    
    
    
#
#This is the plot_cubic function, added for the hell of it, not required course material.
#Basically this is almost a copy and paste of the plot_parabola() function.
#Only difference is the function takes 4 values instead of 3, and has a different format.
#It calculates the curve the exact same way, starting at -14.0 
#
#equation for a cubic curve= ax^3 + bx^2 + cx + d
#
#This uses the same precedure as plot_parabola() where it calculates a startline and endline for x and y.
#The endpoint being x = x + 0.1 and y is calculated at the new x value each time.
#
#
def plot_cubic():
   sys.stderr.write("Equation of a cubic curve: ax^3 + bx^2 + cx + d. Enter in the exponents.\n")
   sys.stderr.write("Please enter the a value: ")
   cubic_a = input()
   sys.stderr.write("Please enter the b value: ")
   cubic_b = input()
   sys.stderr.write("Please enter the c value: ")
   cubic_c = input()
   sys.stderr.write("Please enter the d value: ")
   cubic_d = input()  
   x_startline = swidth_l
   print "color 255 0 255"
   #This while loop will perform calculations for the line end points, plot, then repeat for all x values in the range.
   #The y variables are calculated with the equation of a cubic curve.
   while x_startline <= swidth_r:
    y_startline = cubic_a * x_startline ** 3 + cubic_b * x_startline ** 2 + cubic_c * x_startline + cubic_d
    x_endline = x_startline + paraincrement
    y_endline = cubic_a * x_endline ** 3 + cubic_b * x_endline ** 2 + cubic_c * x_endline + cubic_d
    print "line",convert_x(x_startline),convert_y(y_startline),convert_x(x_endline),convert_y(y_endline)
    x_startline = x_startline + paraincrement
    x_endline = x_endline + paraincrement
    sys.stdout.flush()

#
#This is the convert fractions -> decimal function. This will give the user a decimal approximation of fractions.
#This is to cover the fact that if you enter in an integer fraction value for a constant or coefficient, python does not
#store a decimal value.
def fractionize():
    sys.stderr.write("Fractions are in the form N/D. Numerator Over Demoninator.\n Please enter in N (Numberator): ")
    numerator = input()
    sys.stderr.write("Please enter in D (Denominator): ")
    denominator = input()
    calculated = (numerator + 0.0) / (denominator + 0.0)
    sys.stderr.write("%d/%d is the decimal: %2.5f" % (numerator, denominator, calculated))
    time.sleep(3)
    sys.stdout.flush()
    
  
#
#This is the plot_point function, I was REALLY bored so I decided to have it plot a circle of 2 pixel radius
#on a point the user wants. Nice for checking intersections you've calculated on paper.
def plot_point():
    sys.stderr.write("Please enter in the x coordinate: ")
    x_coord = input()
    sys.stderr.write("Please enter in the y coordinate: ")
    y_coord = input()
    print "color 125 0 25"
    print "fillcircle",convert_x(x_coord),convert_y(y_coord),"2"
    sys.stdout.flush()

#
#The main function.
#This just checks the prompt and executes the correct statement.
#This function also has an error check if a command that doesn't exist is entered, and waits 3 seconds before prompting
#the user a second time.
#
#It's basically an if statement to check if the prompt is one of the existing commands in the program.
#If the prompt matches one of the words, it will call the function.
#If it doesn't, it will say there was an error in the input, and give the user a 3 second pause to read it.
#Then the main prompt will come up again.
#
#
def main():
  plot_axes()
  while True:
   prompt = menu()
   if prompt == "EXIT":
     exit1()
     #break to get out of the loop.
     break
   elif prompt == "LINE":
     plot_line()
     sys.stderr.write("\nCommand Executed!\n")
   elif prompt == "CIRCLE":
     plot_circle()
     sys.stderr.write("\nCommand Executed!\n")
   elif prompt == "CLEAR":
     plot_axes()
     sys.stderr.write("\nCommand Executed!\n")
   elif prompt == "PARABOLA":
     plot_parabola()
     sys.stderr.write("\nCommand Executed!\n")
   elif prompt == "CUBIC":
     plot_cubic()
     sys.stderr.write("\nCommand Executed!\n")
   elif prompt == "CONVERT":
     fractionize()
   elif prompt == "POINT":
     plot_point()
     sys.stderr.write("\nCommand Executed!\n")
   else:
     sys.stderr.write("There was an error in the input, try again.")
     time.sleep(2)
     
#
#This is the only function that needs to be called in order to run the program in its entirety.
main()


