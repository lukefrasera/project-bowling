#!/usr/bin/env python
import sys
sys.path.append('../../')
from drivers.application import application


class BowlingGame(application.Program):
  def __init__(self):
    print "Welcome To Bowling"
    self.running = True

  # def KeyPressEvent(self, e):
  #   while e.Key != '4'
  #     #if e.Key == 'q':
  #       #print "program closing"
  #       #self.running = False
  #     if e.Key == '1'
  #       print "Move pins up to calibrate max"
  #     if e.Key == '2'
  #       print "Move pins down to calibrate max"
  #     if e.Key == '3'
  #       print "Confirm calibrated max"
  #   else 
  #     print "Emergency STOP"

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

  def KeyReleaseEvent(self, e):
    pass

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
  game = BowlingGame()
  a = application.App(game)
  a.Start()

if __name__ == '__main__':
  main()
