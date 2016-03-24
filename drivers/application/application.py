#!/usr/bin/env python
# from Tkinter import *
from pyxhook import HookManager
import time
import signal
from tools import get_char as _getch
import sys

from PyQt4.QtGui import QWidget, QApplication

class Program(QWidget):
  def __init__(self):
    super(Program, self).__init__()
    self.setGeometry(300, 300, 250, 150)
    self.setWindowTitle('Program')
    self.setMouseTracking(True)
  def Start(self):
    self.show()
  def keyPressEvent(self, e):
    if not e.isAutoRepeat():
      self.KeyPressEvent(e)

  def KeyPressEvent(self, e):
    pass
  def keyReleaseEvent(self, e):
    if not e.isAutoRepeat():
      self.KeyReleaseEvent(e)

  def KeyReleaseEvent(self, e):
    pass


class App(QApplication):
  def __init__(self, args):
    super(App, self).__init__(args)

  def Wait(self):
    sys.exit(self.exec_())


# class Program:
#   def __init__(self):
#     self.running = True

#   def KeyPressEvent(self, e):
#     pass

#   def KeyReleaseEvent(self, e):
#     pass

# class App(object):
#   def __init__(self, program):
#     self.program = program

#     signal.signal(signal.SIGINT, self.SignalHandle)
#     self.hooks = HookManager()
#     self.hooks.KeyDown = self.program.KeyPressEvent
#     self.hooks.KeyUp = self.program.KeyReleaseEvent
#     self.hooks.HookKeyboard()
#     self.hooks.start()

#   def Kill(self):
#     self.hooks.cancel()
#   def MainLoop(self):
#     getch = _getch._Getch()
#     while self.program.running:
#       time.sleep(0.1)
#       c = getch()
#     print "Closing the App"
#     self.Kill()
#   def Start(self):
#     self.MainLoop()

#   def SignalHandle(self, signal, frame):
#     print "Ctrl-C: Ending Program"
#     self.hooks.cancel()
#     sys.exit(0)



def main():
  app = App(sys.argv)
  # app = QApplication(sys.argv)
  test = Program()
  # test.show()
  test.Start()
  app.Wait()

if __name__ == '__main__':
  main()
