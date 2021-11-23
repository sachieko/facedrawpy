#Maze Solve Quickdraw 
#Author: @sachieko
#ID: redacted

#Version 1.1
#
#Description: This program will take a text file which the width and height parameters of a maze as its first line.
#The program will then read a text file composed of '*',' ','B','E' where * is a wall, [space] is a space
#and B and E are the beginning and end respectively.
#An example would be:4 4
#                    *E**
#                    * **
#                    * B*
#                    ****
#The lines will be stored into a 2 dimensional list and then using a display function, it will be displayed in
#quickdraw.  Using an algorithm, the maze is then solved, and displayed as it is solved.
#
#
#NOTE: The ability to take an input for the time delay between display functions has issues and hasn't been troubleshooted.
#You need to input files as: python THISPROGRAMPATH.py MAPFILEPATH.txt .05 | java -jar quickdrawPATH.jar
#Where path means you need to declare the path to the program, the text map file, and quickdraw program.
#imported sys to load files and time for the sleep function.
import sys
import time

#
#These are global variables, and represent the different characters that represent parts of a maZe.
#The names should be self explanatory, SOL Being a space marked as part of the Solution and SOLV being
#the final path once the end is reached so it can be highlighted.
WALL = "*"
OPEN = " "
BEGIN = "B"
END = "E"
VISIT = "V"
SOL = "S"
SOLV = "F"

#this variable represents how many pixels across and down the maze is in size, a 500x500 pixel maze by default.
#Only change if you care how big the maze is on the screen in quickdraw.
MAZESIZE = int(500)

#These global variables are the colors of the maze using RGB with a space between
WALLC = "color 120 120 120"
OPENC = "color 0 0 0"
SOLC = "color 0 50 255"
VISITC = "color 255 102 0"
BEGINC = "color 255 0 255"
ENDC = "color 255 0 0"
SOLVC = "color 255 255 255"

#This is the load_maze function. It takes one filename as a parameter, usually given sys.argv[1].
#Then it opens the file and reads the first line and splits it into the slist which has the width and height parameter.
#It then uses the width and height to build an empty list, then it edits the mazefile which is the representation
#of the maze. It will not copy the first line into the list because the first line of a file tells it the height/width
#
#This returns 3 parameters. It returns; the maze as a list, its height, and width. (" ") for size.split?
#
def load_maze(mfilename):
  mfile = open(mfilename,'r')
  size = mfile.readline()
  slist = size.split()
  #slist will be the first characters in the first line, split on a space, and the first 2 characters are width,height.
  width = int(slist[0])
  height = int(slist[1])
  mazefile = []
  #the loop below creates an empty list
  for i in range(width):
    mazefile.append([])
    for j in range(height):
     mazefile[i].append([])
  #this loop loads the maze into the list
  for j in range(height):
     line = mfile.readline()
     for i in range(width):
      mazefile[i][j] = line[i]
  mfile.close()
  #closes the file after reading it
  return mazefile,width,height


#This is the maze solving algorithm that was given to us.
#It takes a list as a parameter, along with the x and y coordinate of the beginning section of the maze.
#and it's width and height, along with how long the maze should pause, usually passed as sys.argv[2]
#
#It will return false or true and mark all new spaces part of the solution until it reaches the end. 
#While the pause parameter doesn't necessarily need to be in here, the old version of the code relied on it heavily.
#Unfortunately due to how the algorithm works, the pause time compounded far too much, and so I moved the actual
#programming for the delay between drawing in quickdraw to the display function.
def solve(list,x,y,width,height,pause):
  display(list,width,height,pause)
  if x < 0 or x >= width or y < 0 or y >= height:
    return False
  elif list[x][y] == WALL or list[x][y] == SOL or list[x][y] == VISIT:
   return False
  elif list[x][y] == END:
     list[x][y] = SOLV
     displayf(list,width,height)
     return True
  
  #mark as part of the solution
  list[x][y] = SOL
    
    
  if solve(list,x-1,y,width,height,pause) == True:
    return True
  if solve(list,x+1,y,width,height,pause) == True:
    return True
  if solve(list,x,y-1,width,height,pause) == True:
    return True
  if solve(list,x,y+1,width,height,pause) == True:
    return True
  
  #if all the above are false, then it will mark the path as not part of the solution but visited.
  list[x][y] = VISIT
  return False
  
#This function is a copy of the display function below, except it only prints after the end has been found.
#It will highlight the found path in white, while leaving the rest the same.
def displayf(maze,width,height):
  print ("flush False")
  print ("color 0 0 0")
  print ("clear")
  w = MAZESIZE/width
  h = MAZESIZE/height
  for i in range(width):
   for j in range(height):
      if maze[i][j] == WALL:
        print (WALLC)
      elif maze[i][j] == OPEN:
        print (OPENC)
      elif maze[i][j] == SOL:
        print (SOLVC)
      elif maze[i][j] == VISIT:
        print (VISITC)
      elif maze[i][j] == BEGIN:
        print (BEGINC)
      elif maze[i][j] == END:
        print (ENDC)
      elif maze[i][j] == SOLV:
        print (SOLVC)
      print ("fillrect %d %d %d %d" % (i*w, j*h, w, h))
      
  print ("refresh")
  sys.stdout.flush()
  
#display image
#It takes the maze, the mazes width, and it's height as parameters.
#It then stops the program from flushing commands and prepares for the next command.
#it calculates the size of each block in the maze from its given width and height.
#It then goes through every block and draws a rectangle of the specified color.
def display(maze,width,height,pause):
  print ("flush False")
  print ("color 0 0 0")
  print ("clear")
  w = MAZESIZE/width
  h = MAZESIZE/height
  for i in range(width):
   for j in range(height):
      if maze[i][j] == WALL:
        print (WALLC)
      elif maze[i][j] == OPEN:
        print (OPENC)
      elif maze[i][j] == SOL:
        print (SOLC)
      elif maze[i][j] == VISIT:
        print (VISITC)
      elif maze[i][j] == BEGIN:
        print (BEGINC)
      elif maze[i][j] == END:
        print (ENDC)
      elif maze[i][j] == SOLV:
        print (SOLVC)
        if maze[i][j] == SOL:
           print(SOLVC)
      print ("fillrect %d %d %d %d" % (i*w, j*h, w, h))
      
  print ("refresh")
  time.sleep(pause)
  sys.stdout.flush()
  


#this is the findstart function, it will find the x and y value in the maze for its beginning.
def findstart(mazef,width,height):
  for i in range(width):
    for j in range(height):
      #searches for the i and j value that represent the start.
      if mazef[i][j] == BEGIN:
        return i,j
        
#this is the main function.
#It will use the two things passed to the program when starting it as the filename (first) then pausetime(second)
#The main function then loads the maze and finds the appropriate variables, and then passes them through
#the findstart() function to find the start of the maze.
#It then displays, and solves the maze.
def main():
  file1 = sys.argv[1]
  pausetime = float(sys.argv[2])
  mazef,width,height = load_maze(file1)

  startx,starty = findstart(mazef,width,height)
  display(mazef,width,height,pausetime)
  solve(mazef,startx,starty,width,height,pausetime)
  displayf(mazef,width,height)
  sys.stderr.write("Solution found, check display.")


#Detects if the file exists or not, if not it closes quickdraw and exits.
try:
    filename = open(sys.argv[1],'r')
except IOError:
    sys.stderr.write("That maze file does not exist in the current directory or folder.")
    print ("quit")
    quit()
else: 
     filename.close()
     
     
     



 #check to make sure all parameters were entered.
try:
   pausecheck = int(float(sys.argv[2]))
    #inform the user of the error and quit.
except IndexError:
    sys.stderr.write("You must enter a maze text file. Example: python programname.py mazefile.txt | java -jar quickdraw.jar")
    print ("quit")
    quit()

    
#Main function which runs the program.
main()



