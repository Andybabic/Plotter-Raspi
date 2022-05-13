


#from libraries.plotter import plotter 
import time
import RPi.GPIO as GPIO

# initialise the plotter
#myPlotter = plotter()
penpin=18
GPIO.setmode( GPIO.BCM)
        # setup the motor control pins
GPIO.setup(penpin,  GPIO.OUT)

for x in range(0, 400): 
    #myPlotter.myPen.putPenDown()
    GPIO.output(penpin, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(penpin, GPIO.LOW)
    #myPlotter.myPen.putPenUp()
    time.sleep(0.2)
        
# close the motor drivers off and lift the pen
#myPlotter.closePlotter()
GPIO.cleanup()