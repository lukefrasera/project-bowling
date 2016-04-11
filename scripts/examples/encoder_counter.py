#!/usr/bin/env python

from time import sleep
import RPIO
from RPIO import PWM
import RPi.GPIO as GPIO
import thread
import time

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
    self.initialized = False
    self.nextPrintTime = 0
    RPIO.add_interrupt_callback(pin_a, self.UpdateState, threaded_callback = True)
    RPIO.add_interrupt_callback(pin_b, self.UpdateState, threaded_callback = True)
    #RPIO.add_interrupt_callback(pin_b, self.UpdateState)
    #RPIO.add_interrupt_callback(pin_a, self.UpdateState)
    thread.start_new_thread(self.encoderWatchdog, ())
  def UpdateState(self, gpio, value):
    self.direction = self.DetectDirection(self.previous_state.pin, self.previous_state.edge, gpio, value, self.direction)
    #print "Direction: %d" % (self.direction)

    if self.direction != 0:
      self.initialized = True

    if self.initialized:
      self.state += self.direction
    #print "Motor Has Turned [%d] degrees" % (self.state / 64.0 * 360.0)
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
  def encoderWatchdog(self):
     while True:
       print self.state
       time.sleep(.5)

class MotorMover:
  def __init__(self, encoder):
    self.encoder = encoder

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)

    self.p = GPIO.PWM(27, 100)
  def TurnMotor(self):
      self.p.start(50)

  def StopMotor(self):
      self.p.stop()
  def SetDirection(self, value):
      GPIO.output(17, (value+1)/2)

  def GoToState(self, state):
      direction = self.encoder.state - state
      direction = direction / abs(direction)
      self.SetDirection(direction)
      self.TurnMotor()
      while self.encoder.state < (state - 10) or self.encoder.state > (state + 10):
          direction = self.encoder.state - state
          direction = direction / abs(direction)
          self.SetDirection(direction)
          time.sleep(.001)
      self.StopMotor()
      print self.encoder.state
###################################################

def main():
  # Initialize program
  encoder = EncoderReader(14, 15)
  motor = MotorMover(encoder)

  RPIO.wait_for_interrupts(threaded=True)
  
  #while True:
  #  value = int(raw_input("Input where to go:"))
  #  print value
  #  motor.GoToState(value)
  #  time.sleep(.2)
  while True:
      motor.GoToState(10000)
      time.sleep(.2)
      motor.GoToState(0)
      time.sleep(.2)


if __name__ == '__main__':
  main()
