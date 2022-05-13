
from config import plotter_config
import decimal 
from decimal import Decimal
import RPi.GPIO as GPIO
import time


class motor:
    
    def __init__(self, pinStep, pinDir, startLen, outwardCW):
        self.pinStep = pinStep
        self.pinSleep = plotter_config.motorSleepPin
        self.pinDir = pinDir
        self.pinStepSize = plotter_config.motorStepSizePin
        self.length= startLen
        self.outwardCW = outwardCW
        # setup the board for BMC (using the names of pin, not physical location)
        GPIO.setmode( GPIO.BCM)
        # setup the motor control pins
        GPIO.setup(self.pinStep,  GPIO.OUT)
        GPIO.setup(self.pinDir,  GPIO.OUT)
        GPIO.setup(self.pinSleep, GPIO.OUT)
        GPIO.setup(self.pinStepSize, GPIO.OUT)
        self.setMotorState(plotter_config.motorWake)
        self.motorStub = False
     
    # set motor direction
    def setMotorDirection(self,direction):
        if self.outwardCW:
            GPIO.output(self.pinDir, not direction)
        else:
            GPIO.output(self.pinDir, direction)
     
    # set motor state (sleep/wake)           
    def setMotorState(self, state):
        GPIO.output(self.pinSleep, state)
      
    # set motor step size
    def setMotorStepSize(self, stepSizeSetting):
        if stepSizeSetting == plotter_config.motorStepCoarse:
            GPIO.output(self.pinStepSize, False)
        else:
            GPIO.output(self.pinStepSize, True) 
         
    def driveMotor(self, direction, lenDelta, duration, stepSizeSetting):
        # identify step size
        if stepSizeSetting == plotter_config.motorStepCoarse:
            stepLen = plotter_config.motorStepLenCoarse
        else:
            stepLen = plotter_config.motorStepLenFine
         
        # check that this motor needs to move at all
        if lenDelta < stepLen:
            # do nothing on this motor
            pass
        else:
            # calc number of steps - use decimal arithmetic to avoid floating point nastiness
            decimal.getcontext().prec = 4
            self.setMotorDirection(direction)
            self.setMotorStepSize(stepSizeSetting)
            # calculate steps needed for length change
            steps = int(Decimal(lenDelta) / Decimal(stepLen))
            lenActualChange = steps * stepLen
            # run the motor
            stepCycleDuration = duration/steps   
            for x in range(0, steps):
                GPIO.output(self.pinStep, GPIO.LOW)
                time.sleep(stepCycleDuration/2)
                GPIO.output(self.pinStep, GPIO.HIGH)
                time.sleep(stepCycleDuration/2)
            if direction == plotter_config.motorDirectionIn:
                self.length = self.length+lenActualChange
            else:
                self.length = self.length-lenActualChange
        
    
         
    def closeMotor(self): 
        self.setMotorState(plotter_config.motorSleep)
        GPIO.cleanup()
