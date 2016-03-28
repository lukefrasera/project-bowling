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
#def ResetPins():
 # RaisePins(6)
  #wait(z_seconds)
  #LowerPins(6)

# # def RaisePins(distance):
# #   TurnPinMotor(100, True, DistToTime(distance))

# # def LowerPins(distance):
#   TurnPinMotor(100, False, DistToTime(distance))

# def DistToTime(dist):
#   return dist

# def TurnMotor(gpio_pin_pwm,gpio_pin_dir,speed,direction,duration):
#   RPIO.setup(gpio_pin_pwm, RPIO.OUT)
#   RPIO.setup(gpio_pin_dir, RPIO.OUT)

#   #if direction:
#    # print "Turning Motor on pin: " + str(gpio_pin_pwm) + "UP"

#   #else:
#    # print "Turning Motor on pin: " + str(gpio_pin_pwm) + "DOWN"
#   RPIO.output(gpio_pin_dir, direction)
#   RPIO.output(gpio_pin_pwm, True)
#   sleep(duration)
#   RPIO.output(gpio_pin_pwm, False)
#   print "Done Moving"
#   RPIO.cleanup()

# def TurnPinMotor(speed,direction,duration):
#   TurnMotor(19,6,speed,direction,duration)

################ENCODER COUNTER
def Encoder(channel_A,channel_B):
  RPIO.setup(channel_A, RPIO.IN)
  RPIO.setup(channel_B, RPIO.IN)

  previous_A = RPIO.input(channel_A)
  previous_B = RPIO.input(channel_B)
  index_A = 0
  index_B = 0
  edge_A = -1
  edge_B = -1
  previous_change = ''
  current_change = ''
  while True:
    value_A = RPIO.input(channel_A)
    value_B = RPIO.input(channel_B)
    if value_A != previous_A:
      current_change = 'a'
      index_A += 1
      print 'A Changed: %d times' % (index_A)
      if value_A == True:
        edge_A = True
      else:
        edge_A = False
      previous_change = current_change


    if value_B != previous_B:
      current_change = 'b'
      index_B += 1
      print 'B Changed: %d times' % (index_B)
      if value_B == True:
        edge_B = True
      else:
        edge_B = False
      previous_change = current_change


    previous_A = value_A
    previous_B = value_B




















      
def DetectDirection(previous_change, previuos_type, current_change, current_type, previous_direction):
  if previous_change == 'a' and current_change == 'b':
    # A happened and then B ==> A | B
    if current_type == True and previuos_type == False:
      direction = -1
    if current_type == False and previuos_type == True:
      direction = -1

    if current_type == True and previuos_type == True:
      direction = 1
    if current_type == False and previuos_type == False:
      direction = 1

  if previous_change == 'b' and current_change == 'a':
    if current_type == True and previuos_type == False:
      direction = 1
    if current_type == False and previuos_type == True:
      direction = 1
    if current_type =- True and previuos_type == True:
      direction = -1
    if current_type =- False and previuos_type == False:
      direction = -1
  if previous_change == current_change:
    direction = -previous_direction


##Counter Clockwise
  #if RPIO.input(6) == 'True'

  # if RPIO.input(14) == 'False' & RPIO.input(15) == 'False'
  # if RPIO.input(14) == 'False' & RPIO.input(15) == 'True'
  # if RPIO.input(14) == 'True' & RPIO.input(15) == 'True'  
  # if RPIO.input(14) == 'True' & RPIO.input(15) == 'False' 
##Clockwise
  #if RPIO.input(6) == 'False'

  # if RPIO.input(14) == 'True' & RPIO.input(15) == 'False' 
  # if RPIO.input(14) == 'True' & RPIO.input(15) == 'True' 
  # if RPIO.input(14) == 'False' & RPIO.input(15) == 'True'
  # if RPIO.input(14) == 'False' & RPIO.input(15) == 'False'
def ChannelAHigh():
  count() 

###################################################

def main():
  # Initialize program
  Encoder(14,15)

if __name__ == '__main__':
  main()
