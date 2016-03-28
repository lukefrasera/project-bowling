#!/usr/bin/env python

from time import sleep
import RPIO
from RPIO import PWM

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


class GPIOState:
    def __init__(self, init_pin, init_edge):
        self.pin = init_pin
        self.edge = init_edge

class EncoderReader:
  def __init__(self, pin_a, pin_b):
    # Initialize GPIO Callbacks
    self.pin_a = pin_a
    self.pin_b = pin_b
    self.previous_state = GPIOState(-1,-1)
    self.state = 0
    self.direction = 0

    RPIO.add_interrupt_callback(pin_a, self.UpdateState, threaded_callback=True)
    RPIO.add_interrupt_callback(pin_b, self.UpdateState, threaded_callback=True)

  def UpdateState(self, gpio, value):


    self.direction = self.DetectDirection(self.previous_state.pin, self.previous_state.edge, gpio, value, self.direction)
    print "Direction: %d" % (self.direction)
    self.previous_state.pin = gpio
    self.previous_state.edge = value

  def DetectDirection(self, previous_change, previous_type, current_change, current_type, previous_direction):
    direction = 0
    if previous_change == self.pin_a and current_change == self.pin_b:
      # A happened and then B ==> A | B
      if current_type == True and previous_type == False:
        direction = -1
      if current_type == False and previous_type == True:
        direction = -1

      if current_type == True and previous_type == True:
        direction = 1
      if current_type == False and previous_type == False:
        direction = 1

    if previous_change == self.pin_b and current_change == self.pin_a:
      if current_type == True and previous_type == False:
        direction = 1
      if current_type == False and previous_type == True:
        direction = 1
      if current_type == True and previous_type == True:
        direction = -1
      if current_type == False and previous_type == False:
        direction = -1
    if previous_change == current_change:
      direction = -previous_direction

    return direction

###################################################

def main():
  # Initialize program
  encoder = EncoderReader(14, 15)

  RPIO.wait_for_interrupts()

  while True:
    pass

if __name__ == '__main__':
  main()
