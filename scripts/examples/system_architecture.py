#!/usr/bin/env python
'''
resets pins after a key input
first raises, then lowers pins

'''
from time import sleep

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
  RaisePins(10)
  #wait(z_seconds)
  LowerPins(20)

def RaisePins(distance):
  TurnPinMotor(100, True, DistToTime(distance))

def LowerPins(distance):
  TurnPinMotor(100, False, DistToTime(distance))

def DistToTime(dist):
  return dist/2

def TurnMotor(gpio_pin_pwm,gpio_pin_dir,speed,direction,duration):
  if direction:
    print "Turning Motor on pin: " + str(gpio_pin_pwm) + "UP"
  else:
    print "Turning Motor on pin: " + str(gpio_pin_pwm) + "DOWN"
  sleep(duration)
  print "Done Moving"


def TurnPinMotor(speed,direction,duration):
  TurnMotor(17,16,speed,direction,duration)

###################################################

def main():
  # Initialize program
  print "Initializing program: Getting ready..."
  get_char = _Getch()
  print "Program Ready!"
  # Main loop
  while True:
    ch = get_char()
    # if button pressed
    if ch:
      # if key == r
      if ch =='r':
        print "Resetting Pins"
        ResetPins()
      # if key doesn't = r
      elif ch == 'q':
        break
      else:
        print "Key not recognized"
  # close program
  print "Closing Program: Thanks for Playing"

if __name__ == '__main__':
  main()
