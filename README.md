For reference: QuickDraw is a program which can take input from a python script and create graphics on the screen with this input.

# facedrawpy
First python project: FaceDraw

First Project: Asks user to input coordinates, draws a predetermined image on those coordinates using a program that uses python input to create a graphical image
Intermediary program is called Quickdraw

Second Project: Python Ball Simulation
Using Quickdraw again, the user inputs whether a ball will start with or without vertical velocity (gravity variable only), then graphically draws the ball in a simulation and outputs its position to the user. 

Third Project: This project takes input in the form of a textfile which lists the RGB values of the pixels in an image, and can display the image. Then it has a few image processing capabilities built into it. Much of the project is devoted to creating lists which represent the image, and performing operations on those lists which will be returned back to Quickdraw in a format which let it print its way.
Zoom: Zooms into the image. 
Rotate: Rotates image
Chromakey: Will replace certain shades of green with the image of another image, allowing you to place part of one image onto another's background.
Other features such as greyscale or sepia are possible with modification.

Fourth Project: Maze solving Project
This program takes a text file input which represents a maze, and then graphically displays the maze. Then it automatically starts to proceed through the maze from the designated start, and highlights the path it takes. If it has to backtrack, the incorrect path will change color to indicate it backtracked, and this continues until it finds the exit. This uses a standard maze solving algorithm of taking the rightmost path each time, avoiding paths it has already gone down.
