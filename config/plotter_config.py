

import os
import socket

# Deployment environment switch - running as debugMode stubs out all GPIO functions
plotterHostname = socket.gethostname()
if socket.gethostname() == plotterHostname:
    # todo put debug value into the plotter class
    #debugMode = True
    debugMode = False
else:
    debugMode = True

# Motor Physics
motorRevCircumference = 36  # circumference of motor spigot in mm
penSpeed = 20  # mm per second
motorStepsPerRevCoarse = 200
motorStepWaitCoarse = penSpeed/motorStepsPerRevCoarse  # 0.02
motorStepLenCoarse = motorRevCircumference/motorStepsPerRevCoarse  # 0.2 for this plotter
motorStepsPerRevFine = 200
motorStepLenFine = motorRevCircumference/motorStepsPerRevFine  # 0.025 for this plotter
motorStepWaitFine = penSpeed/motorStepsPerRevFine  # 0.0025

# Plotter Dimensions in mm
marginTop = 400  # vertical distance between the centre of the motor spindle and the top of the paper (draw space)
marginSide = 180  # horizontal distance between the point on the inside edge of the motor spindle and the left hand paper edge
paperHeight = 300  # max plot height of the image
motorGap = 580  # horizontal distance between the point on the inside edge of the two motor spindles
paperWidth = motorGap - 2 * marginSide  # 540mm with the current set up

# Plotter Setup - pen at top left corner of the paper
startx = 0
starty = paperHeight
penReplacementPosx = 0
penReplacementPosy = 0

# Enumerate states used in control code
motorSleep = False
motorWake = True
motorDirectionOut = True
motorDirectionIn = False
motorStepCoarse = True
motorStepFine = False
floatToCell = False
drawToCell = True

# pen ink replacement
penReplacement = True  # will halt the plot when the capacity of pen ink is used.
penReplacementLength = 250000  # mm of line
if debugMode:
    # don't pause the pen in debug (emulator) mode
    penReplacement = False

# Motor Controls GPIO settings
# motorR controls
motorRStep = 6
motorRDir = 13

#motorL controls
motorLStep = 19
motorLDir = 26 
motorSleepPin = 21
motorStepSizePin = 12
penpin=18
#GPIO.setup(penpin,  GPIO.OUT)



# Pen Lift - Servo commands used by servo blaster
penGPIOSetupCommand = 'GPIO.setup(18, GPIO.OUT)'  # maps servo to GPIO-18
penDownCommand = 'GPIO.output(18, GPIO.HIGH)'  # 35
penUpCommand = 'GPIO.output(18, GPIO.HIGH)'  # 5

# Render properties
minimumLineLen = 0.5  # mm the plotter will not attempt to draw lines shorter than this
maximumLineLen = 2  # the plotter will segment lines greater than this to avoid 'droop' artifacts

# Source image location
imageDirectory = "images"

# Emulator and SVG output
emulatorDirectory = "emulated"
onScreenEmulator = True

