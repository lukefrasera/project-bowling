#!/usr/bin/env python
import sys
sys.path.append('../../')
from drivers.application import application


class BowlingGame(application.Program):
  def __init__(self):
    print "Welcome To Bowling"
    self.running = True

  def KeyPressEvent(self, e):
    if e.Key == 'q':
      print "program closing"
      self.running = False

  def KeyReleaseEvent(self, e):
    pass


def main():
  game = BowlingGame()
  a = application.App(game)
  a.Start()

if __name__ == '__main__':
  main()
