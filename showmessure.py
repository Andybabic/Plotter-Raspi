

import math

from config import plotter_config
from libraries.emulator import emulator
from libraries.plotter import plotter
from libraries.pointList import pointList
#from libraries.svg import svgHandler
from svg.path import parse_path
from svg.path.path import Line
from xml.dom import minidom



#from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, Close


# initialise the plotter
myPlotter = plotter()
myPlotter.penSetup()

# converts a list of path elements of a SVG file to simple line drawing commands
scale= 0.9
imageXCentre = plotter_config.paperWidth / 2
imageYCentre = plotter_config.paperHeight / 2

waitpen= True

moveX=50
moveY=-30

saveX= 0
saveY= 0
# read the SVG file
#doc = minidom.parse('libraries/test.svg')
doc = minidom.parse('svgs/emmaich12.svg')
path_strings = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
#print(path_strings)
#doc.unlink()

# print the line draw commands

myPlotter.floatToPoint((plotter_config.paperWidth), (0))
myPlotter.floatToPoint((plotter_config.paperWidth), (plotter_config.paperWidth)) 
myPlotter.floatToPoint((0), (plotter_config.paperWidth))
myPlotter.floatToPoint((0), (0))

                
                
            
                
           
                
response = input()
myPlotter.closePlotter()
input()


    