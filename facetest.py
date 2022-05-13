
import math

from config import plotter_config
from libraries.emulator import emulator
from libraries.plotter import plotter
from libraries.pointList import pointList
#from libraries.svg import svgHandler
from svg.path import parse_path
from svg.path.path import Line
from xml.dom import minidom
import os



#from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, Close


# initialise the plotter
myPlotter = plotter()
myPlotter.penSetup()

# converts a list of path elements of a SVG file to simple line drawing commands
scale= 0.7
imageXCentre = plotter_config.paperWidth / 2
imageYCentre = plotter_config.paperHeight / 2

waitpen= True

moveX=-0
moveY=40

saveX= 0
saveY= 0
# read the SVG file
#doc = minidom.parse('libraries/test.svg')
doc = minidom.parse('svgs/jesusfin_pen0.svg')
path_strings = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
#print(path_strings)
#doc.unlink()

# print the line draw commands
for path_string in path_strings:
    print('loop'+path_string)
    path = parse_path(path_string)
    for e in path:
        if isinstance(e, Line):
            x0 =   e.start.real  *scale + moveX
            y0 =   e.start.imag  *scale + moveY
            x1 =   e.end.real *scale + moveX
            y1 =   e.end.imag *scale+ moveY
            saveX= x0
            saveY= y0
            
#             print("(%.2f, %.2f) - (%.2f, %.2f)" % (x0, y0, x1, y1))
            
            while True:
                if True:
                #if os.path.exists("cropped_face/face_.jpg"):
                    if e == 0:
                        # float to the start point (for the first shape only)
                        myPlotter.floatToPoint((x0), (y0))
                        myPlotter.drawToPoint((x1 ), (y1 ),plotter_config.motorStepFine)
                    
                    else:
                        # draw to the start point
                        myPlotter.drawToPoint((x0 ), (y0 ),plotter_config.motorStepFine)
                        myPlotter.drawToPoint((x1 ), (y1 ),plotter_config.motorStepFine)
                    break
            
                
            if waitpen:
                response = input()
                waitpen =False
                
response = input()
myPlotter.closePlotter()
input()


    