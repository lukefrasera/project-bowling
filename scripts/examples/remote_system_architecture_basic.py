#!/usr/bin/env python
'''
resets pins after a key input
first raises, then lowers pins

'''
from time import sleep
import RPIO
from RPIO import PWM
import serial
################################################################################
################################# DO NOT TOUCH #################################
################################################################################
class _Getch:
  '''
  Gets a single character from standard input.  Does not echo to the screen.
  '''
  def __init__(self):
    try:
      self.impl = _GetchWindows()
    except ImportError:
      self.impl = _GetchUnix()

  def __call__(self): return self.impl()


class _GetchUnix:
  def __init__(self):
    import tty, sys

  def __call__(self):
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '\x03':
      raise KeyboardInterrupt
    return ch


class _GetchWindows:
  def __init__(self):
    import msvcrt

  def __call__(self):
    import msvcrt
    return msvcrt.getch()
################################################################################


#################### FUNCTIONS ####################
def ResetPins(loweringtime):
  RaisePins(raisingtime)
  #wait(z_seconds)
  LowerPins(loweringtime)

def RaisePins(distance):
    TurnPinMotor(100, True, DistToTime(distance))


def LowerPins(distance):
  TurnPinMotor(100, False, DistToTime(distance))

def StorePins(distance):
  TurnPinMotor(100, True, DistToTime(distance))

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
  #RPIO.cleanup()

def TurnPinMotor(speed,direction,duration):
  TurnMotor(19,6,speed,direction,duration)

###################################################

def main():
  # Initialize program
  print "Initializing program: Getting ready..."
  get_char = _Getch()
  print "Program Ready!"
  # Main loop
  ser = serial.Serial('/dev/ttyUSB0', 9600)
  # flush serial buffer so that all previous commands are removed
  ser.flush() 
  sleep(.1) # wait for the buffer to be freed
  ###Calibration - new
  loweringtime = 0
  raisingtime = 0
  print "In play state"
  while True:
    button = ser.read(1)
    #button 1
    if button == '\x01':
      #lower for as long as button is pressed
      LowerPins(0.25)
      loweringtime += 0.25
    #button 2
    if button == '\x00':
      #raise for as long as button is pressed
      RaisePins(0.25)
      raisingtime += 0.25
    
    #button 3
    if button == '\x03':
      pass
   
   #button 4
    if button == '\x02':
      # break
      quit()

    ser.flushInput()
    sleep(0.1)
  print "In store and quit state"
###Play - old
  # storetime = 0
  # while True:
  #   button = ser.read(1)
  #   #button 1
  #   if button == '\x01':
  #     pass
  #   #button 2
  #   if button == '\x00':
  #     pass
  #   #button 3
  #   if button == '\x03':
  #     #raises pins for as long as button is held
  #     StorePins(0.25)
  #     storetime += 0.25
  #   #button 4
  #   if button == '\x02':
  #     #quits/closes program
  #     quit()
    # ser.flushInput()
    # sleep(0.1)
  # close program



if __name__ == '__main__':
  main()
