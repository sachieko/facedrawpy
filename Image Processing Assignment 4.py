#Image Processing Assignment 4
#ID: BLANKED
#
#Author: @sachieko
#
#NOTE: when running the program in quickdraw, if the java heap space runs out, increase the java heap
#by using:  programname.py | java -Xmx512M -jar quickdraw.jar
#
#To create several functions which perform image processing tasks.
#
#Supporting functions will be used, such as functions to compute the height and width of an image.
#Also a create image function will create a list used to create a new image.
#A display image function was also created. This will display an image which will be a list of lists of lists.
#
#A chromaKey function will cause all the green pixels in an image to be replaced with pixels of a new image.
#This function will return the new list. 
#
#A rotate90cw function will take a picture and rotate all the pixels in a list 90 degrees (pi/2 radians)
#and return the new list to be displayed as a rotated picture.
#
#The last function to be created is a zoom function which will take a portion of a picture, and zoom in on
#the picture by an INTEGER zoom factor. floating point numbers cannot work for the zoom function in its current state.
#The zoom function will then return a new list of the same dimensions, but zoomed in on the center of the image.
#
#I have included a main function which will be used to demonstrate each of the three functions.
#

import ppm 
import sys


#These are for the order in which the red green and blue factors of a pixel are displayed in the list.
#ie: image[x][y][index] where index = RED, GREEN, BLUE.
RED = 0
GREEN = 1
BLUE = 2

#These variables are how much the green value of a pixel must be above the other color to be considered green.
#This is used for the chromaKey function.
GREENRED = 20
GREENBLUE = 50

#IMPORTED FOR USE IN MAIN()
#This function converts the input into capitals to avoid case sensitive errors.
#It takes whatever input was given and converts it into all capital letters.
def convertinput():
   global prompt
   prompt = prompt.upper()
   
#
#This is a copy of code developed in class.
#Original comments by Ben Stephenson:
#  Create a list of list of lists that represent an empty image
#  400 pixels across by 200 pixels high.  All colors in the image
#  are black
#
#Returns the image as a list.
def createImage(width,height):
  image = []
  for i in range(0,width):
   image.append([])
   for j in range(0,height):
    image[i].append([0,0,0])
  return image

#
#This is the width function. It computes the number of columns of pixels in the
#image, and returns this number.
def width(image):
  return len(image)

#this is the height function. It computes the number of rows of pixels in the image, returns this number.
#It uses a zero for the first index of lists.
def height(image):
  return len(image[0])


#
#This is the displayImage function
#Other than the fact that width and height are calculated now, the majority of this code was
#developed in class for displaying an image.
#
#Original comments by Ben Stephenson:
#
#  Display the picture in QuickDraw
#
#  The pixels primitive gives us a way to draw many primitives using a single
#  QuickDraw command, which is much faster than drawing each pixel 
#  individually.  Note that the command doesn't end until the final
#  print "" because the comma at the end of the line for the earlier 
#  print statements prevents them from advancing to the next line.
#
def displayImage(x,y,image):
  width1 = width(image)
  height1 = height(image)
  print "pixels",x,y,width1,height1,
  for y in range(0,height1):
   for x in range(0,width1):
    print image[x][y][RED],image[x][y][GREEN],image[x][y][BLUE],
  print ""
  sys.stdout.flush()

#Test Cases-
#picture = ppm.load_ppm("Chipmunk2.ppm")
#displayImage(0,0,picture)
#
#picture2 = ppm.load_ppm("Parrot.ppm")
#displayImage(width(picture),0,picture2)
#
#IMPORTANT NOTE: When I originally ran these tests, I accidentally chromaKeyed. Use this for a later function haha.
#This chromaKey error was accidentally using the word picture instead of image for 2 cases in displayImage.


#
#This is the chromaKey function. It takes two parameters, a top image and a bottom image.
#It takes the minimum of their heights and widths for the universal height and widths.
#Then it copies the displayImage function pretty much, 0 being the default starting area to print an image.
#The function then checks if the green component (topimage[x][y][1]) meets the requirements to make the pixel
#green.
#If the current pixel in the FOR loop meets the requirements for a green pixel (+20 than the red component and
# +50 than the blue component.) then it takes the color info from the bottom image and updates the pixels with
#the bottom image input.
#
#Else, it prints the top image. 
#red is imagename[x][y][0], green = imagename[x][y][1], blue = imagename[x][y][2]
#
#This will return the new image as a list.
def chromaKey(topimage,botimage):
   width1 = min(width(topimage),width(botimage))
   height1 = min(height(topimage),height(botimage))
   chromaImage = createImage(width1,height1)
   for y in range(0,height1):
     for x in range(0,width1):
      if topimage[x][y][GREEN] > topimage[x][y][RED] + GREENRED and topimage[x][y][GREEN] > topimage[x][y][BLUE] + GREENBLUE:
        chromaImage[x][y] = botimage[x][y]
      else: 
        chromaImage[x][y] = topimage[x][y]
   return chromaImage


#Test Case-
#picture1 = ppm.load_ppm("Lion.ppm")
#picture2 = ppm.load_ppm("HelloWorld.ppm")
#
#picture3 = chromaKey(picture2,picture1)
#displayImage(0,0,picture3)

#
#
#This is the Rotation function. It takes an image as a parameter.
#It uses the images height for it's width, and it's width for it's new height.
#Then the For loop flips the pixels in the given image, and puts them in a different order.
#This results in what appears to be an invert, where the image has been picked up and flipped
#over a line described as y = x mathematically. This is not a 90 degree rotation.
#
#In order to correct this, the only thing that is incorrect, is the order of the pixels in the images width.
#So the list.reverse() function is used and will flip the WIDTH of the list, making it appear to be a correct rotation.
#Produced, is a 90 degree rotation.
#
#This returns the rotated image as a new list.
def rotate90CW(image):
  width1 = height(image)
  height1 = width(image)
  rotImage = createImage(width1,height1)
  for x in range(0,width1):
   for y in range(0,height1):
    rotImage[x][y] = image[y][x]
  rotImage.reverse()
  return rotImage
  
#Test Case
#picture1 = ppm.load_ppm("Chipmunk2.ppm")
#picture2 = rotate90CW(picture1)
#displayImage(0,0,picture2)




#  - - - - 
#  - - - -     
#This is the zoom function.
#It takes an image and zoom factor as a parameter (zoomf)
#It computes the width and height of the image to return from the original image
#It then computes how much of the picture it will skip past before it starts to copy pixels.
#
#zoom1 and zoom2 determine the upper and lower bound for how many pixels to copy into a block.
#Then for each i in the width, zoom1 is increased by the zoom factor.
#This repeats for every j in the width, zoom 2 is increased.
#
#The formula for finding the area zoomed in on determined from their dimensions is:
#
#zoomed dimension = (original - original/zoomfactor) / 2
#this is used for width and height.
#
#This Returns a dimensional list which represents the zoomed in image.
#
def zoom(image,zoomf):
  width1 = width(image)
  height1 = height(image)
  zoomheight = (height1 - height1 / zoomf) / 2
  zoomwidth = (width1 - width1 / zoomf) / 2
  zoomImage = createImage(width1,height1)
  zoom1 = 0
  zoom2 = 0
  #this range is every width in the zoomed in section of the image.
  for i in range(zoomwidth,width1-zoomwidth):
      zoom1 = zoom1 + zoomf
      zoom2 = 0
      #this if statement prevents the program from crashing with an index error.
      if zoom1 >= width1:
       zoom1 = 0
      #this range is every height in the zoom height section of the image.
      for j in range(zoomheight,height1-zoomheight):
       #everytime j increased, zoom2 increases in height.
       zoom2 = zoom2 + zoomf
       #prevents crash from an index error.
       if zoom2 >= height1:
         zoom2 = 0
       for k in range(zoom1-zoomf,zoom1):
          for n in range(zoom2-zoomf,zoom2):
            zoomImage[k][n] = image[i][j]
  return zoomImage
  
#Test Case - FINALLY WORKED SUCCESSFULLY
#picture1 = ppm.load_ppm("DonaldDuck.ppm")
#picture2 = zoom(picture1,3)
#displayImage(0,0,picture1)
#displayImage(width(picture1),0,picture2)
#picture3 = zoom(picture1,5)
#displayImage(width(picture1),0,picture3)

def main():
    while True: 
      global prompt
      sys.stderr.write('To test one of the image functions,\n please type a command(chromakey, rotate, zoom, zoom2, zoom3, exit):')
      prompt = raw_input()
      convertinput() 
      if prompt == "CHROMAKEY":
        picture1 = ppm.load_ppm("HelloWorld.ppm")
        picture2 = ppm.load_ppm("Tucan.ppm")
        picture3 = ppm.load_ppm("HaLingPeak.ppm")
        displayImage(0,height(picture1),picture2)
        picture4 = chromaKey(picture1,picture3)
        picture5 = chromaKey(picture2,picture4)
        displayImage(0,0,picture4)
        displayImage(width(picture4),0,picture5)
      elif prompt == "ROTATE":
        picture1 = ppm.load_ppm("Lion.ppm")
        picture2 = rotate90CW(picture1)
        picture3 = rotate90CW(picture2)
        displayImage(0,0,picture1)
        displayImage(width(picture1),0,picture2)
        displayImage(0,height(picture1),picture3)
        picture1 = ppm.load_ppm("Chipmunk2.ppm")
        picture2 = rotate90CW(picture1)
        displayImage(0,0,picture1)
        displayImage(width(picture1),0,picture2)
      elif prompt == "ZOOM":
        picture1 = ppm.load_ppm("DonaldDuck.ppm")
        picture2 = zoom(picture1,2)
        picture3 = zoom(picture1,3)
        picture4 = zoom(picture1,4)
        picture8 = zoom(picture1,8)
        displayImage(0,0,picture1)
        displayImage(0,0,picture2)
        displayImage(0,0,picture3)
        displayImage(0,0,picture4)
        displayImage(0,0,picture8)
      elif prompt == "ZOOM2":
        picture1 = ppm.load_ppm("Chipmunk2.ppm")
        picture2 = zoom(picture1,2)
        picture3 = zoom(picture1,3)
        picture4 = zoom(picture1,4)
        picture8 = zoom(picture1,8)
        displayImage(0,0,picture1)
        displayImage(0,0,picture2)
        displayImage(0,0,picture3)
        displayImage(0,0,picture4)
        displayImage(width(picture1),0,picture8)
      elif prompt == "ZOOM3":
        picture1 = ppm.load_ppm("MinnieMouse.ppm")
        picture2 = zoom(picture1,2)
        picture3 = zoom(picture2,2)
        picture4 = zoom(picture3,2)
        displayImage(0,0,picture1)
        displayImage(0,0,picture2)
        displayImage(0,0,picture3)
        displayImage(0,0,picture4)
      elif prompt == "EXIT":
        print "quit"
        break

main()






