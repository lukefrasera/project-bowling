#!/usr/bin/env python

import logging
from RPIO import PWM as pwm

class MotorDriver(object):
  def __init__(self):
    logging.debug("Generating Motor Driver")


def testing():
  driver = MotorDriver()

if __name__ == '__main__':
  testing()