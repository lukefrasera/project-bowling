#!/usr/bin/env python
'''
resets pins after a key input
first raises, then lowers pins

'''
from time import sleep
import RPIO
from RPIO import PWM

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
def ResetPins():
  RaisePins(6)
  #wait(z_seconds)
  LowerPins(6)

def QuickPins():
  RaisePins(2)
  LowerPins(2)

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
  TurnMotor(9,11,speed,direction,duration)
  #test test to save

###################################################

def main():
  RPIO.setup(6,RPIO.IN)
  RPIO.setup(13,RPIO.IN)
  RPIO.setup(26,RPIO.IN)
  while True:
    if RPIO.input(6):
      ResetPins()
    if RPIO.input(13):
      QuickPins()
    if RPIO.input(26):
      break

if __name__ == '__main__':
  main()
