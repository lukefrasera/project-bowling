#!/usr/bin/env python
import sys
import time
import os


sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),'../../'))
from drivers.application import application

class State:
  def __init__(self):
    #self.BEGIN = 0
    self.CALIBRATE = 1
    self.PLAY = 2
    self.QUIT = 3


class BowlingGame(application.Program):
  def __init__(self):
    super(BowlingGame, self).__init__()
    print "Welcome To Bowling"
    self.running = True
    self.state = State().CALIBRATE
    self.calibrate_part = 0

  def Start(self):
    self.show()

  def Quit(self):
    #pass
    print 'Quit'

  def KeyPressEvent(self, e):
    # Check which state I am in
    #if self.state == State().BEGIN:
      #Do the begin KEYs
     # pass
    if self.state == State().CALIBRATE:
      # Do the keys for calibration
      if e.text() == '4':
        self.Quit()
      if e.text() == '3':
        if self.calibrate_part == 0:
          print 'Save Max Encorder value'
          self.encoder_max = 'max'
          self.calibrate_part = 1
        elif self.calibrate_part == 1:
          print 'Save Min Encoder value; Ready to play'
          #print 'ready to play'
          self.encoder_min = 'min'
          self.state = State().PLAY
      if e.text() == '2':
        print 'start moving pins down'
      if e.text() == '1':
        print 'start moving pins up'
        
    if self.state == State().PLAY:
      # do the keys for PLAY
      if e.text() == '1':
        print 'Reset Pins'
      if e.text() == '2':
        print 'Store Pins'
      if e.text() == '4':
        self.Quit()
    if self.state == State().QUIT:
      # do keys for quit
      pass
        

  def KeyReleaseEvent(self, e):
    #if self.state == State().BEGIN:
      #Do the begin KEYs
     # pass
    if self.state == State().CALIBRATE:
      # Do the keys for calibration
      if e.text() == '1':
        print 'stop pins up'
      if e.text() == '2':
        print 'stop pin down'
      if e.text() == '3':
        pass
      if e.text() == '4':
        pass
    if self.state == State().PLAY:
      # do the keys for PLAY
      pass
    if self.state == State().QUIT:
      # do keys for quit
      pass



    # while e.Key != '4'
    #   #if e.Key == 'q':
    #     #print "program closing"
    #     #self.running = False
    #   if e.Key == '1'
    #     print "Move pins up to calibrate max"
    #   if e.Key == '2'
    #     print "Move pins down to calibrate max"
    #   if e.Key == '3'
    #     print "Confirm calibrated max"
    # else 
    #   print "Emergency STOP"

  def CalibrateMax(self, e):
    while e.Key != '4':
      #if e.Key == 'q':
        #print "program closing"
        #self.running = False
      if e.Key == '1':
        print "Move pins up to calibrate max"
      if e.Key == '2':
        print "Move pins down to calibrate max"
      if e.Key == '3':
        print "Confirm calibrated max"
    else: 
      print "Emergency STOP"

  def CalibrateMin(self, e):
    while e.Key != '4':
      #if e.Key == 'q':
        #print "program closing"
        #self.running = False
      if e.Key == '1':
        print "Move pins up to calibrate min"
      if e.Key == '2':
        print "Move pins down to calibrate min"
      if e.Key == '3':
        print "Confirm calibrated min"
    else: 
      print "Emergency STOP"


  def InitiateCalibration(button):
    CalibrateMax()
    CalibrateMin()

  # def CalibrateMax(): #how to make is optional to move both up and down before setting?
  #   KeyPressEvent(1)
  #     print "Move pins up to calibrate max"
  #   KeyPressEvent(2)
  #     print "Move pins down to calibrate max"
  #   KeyPressEvent(3)
  #     print "Confirm calibrated max"
  # def CalibrateMin(): #how to make is optional to move both up and down before setting?
  #   KeyPressEvent(1)
  #     print "Move pins up to calibrate min"
  #   KeyPressEvent(2)
  #     print "Move pins down to calibrate min"
  #   KeyPressEvent(3)
  #     print "Confirm calibrated min"
  def BeginPlay():
    while e.Key != '4':
      #if e.Key == 'q':
        #print "program closing"
        #self.running = False
      if e.Key == '1':
        #print "Coil up pins: Motor ON, Motor Dir TRUE, until calibrated max; Uncoil pins: Motor ON, Motor Dir FALSE, until calibrated min"
        RaisePins() #until encoder max
        print "Raise pins"
      if e.Key == '2':
        #print "Coil up pins for storage: Motor ON, Motor Dir TRUE, until calibrated max"
        LowerPins() #until encoder min
        print "Lower pins"
      # if e.Key == '3'
      #   print "Confirm calibrated min"
    else: 
      print "Emergency STOP"
#test comment
def RaisePins(distance):
  TurnPinMotor(100, True, DistToTime(distance))

def LowerPins(distance):
  TurnPinMotor(100, False, DistToTime(distance))

def DistToTime(dist):
  return dist

def TurnMotor(gpio_pin_pwm,gpio_pin_dir,speed,direction,duration):
  RPIO.setup(gpio_pin_pwm, RPIO.OUT)
  RPIO.setup(gpio_pin_dir, RPIO.OUT)

  if direction:
    print "Turning Motor on pin: " + str(gpio_pin_pwm) + "UP"

  else:
    print "Turning Motor on pin: " + str(gpio_pin_pwm) + "DOWN"
  RPIO.output(gpio_pin_dir, direction)
  RPIO.output(gpio_pin_pwm, True)
  sleep(duration)
  RPIO.output(gpio_pin_pwm, False)
  print "Done Moving"
  RPIO.cleanup()

def TurnPinMotor(speed,direction,duration):
  TurnMotor(19,6,speed,direction,duration)

def main():
  a = application.App(sys.argv)
  game = BowlingGame()
  game.Start()
  a.Wait()

if __name__ == '__main__':
  main()
