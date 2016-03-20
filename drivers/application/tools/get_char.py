# from Tkinter import *
import select
# import sys
import time
import sys, tty, termios
# import pygame
import os

def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

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
        # tty.setcbreak(sys.stdin.fileno())
        if isData():
          print "is Data"
          ch = sys.stdin.read(1)
        else:
          ch = None
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


class PollKeyboard:
  def __init__(self, timeout):
    self.read_list = [sys.stdin]
    self.timeout = timeout

  def __call__(self):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
      tty.setraw(sys.stdin.fileno())
      if select.select(self.read_list, [], [], self.timeout)[0]:
        ch = sys.stdin.read(1)
      else:
        ch = None
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '\x03':
      raise KeyboardInterrupt
    return ch



def keydown(e):
  print "pressed: ", e.char

def keyup(e):
  print "released: ", e.char

def main():
  # get_char = PollKeyboard(0.1)
  # while True:
  #   ch = get_char()
  #   if ch:
  #     if ch == 'l':
  #       print "You Pressed L"
  #     else:
  #       print "you didn't press L"
  #   else:
  #     print "hello"

    # if not sys.stdin.isatty():
    #   print "not sys.stdin.isatty"
    # else:
    #   print "is  sys.stdin.isatty"

  os.system('xset r off')
  try:
    root = Tk()
    frame = Frame(root, width=100, height=100)
    frame.bind("<KeyPress>", keydown)
    frame.bind("<KeyRelease>", keyup)
    frame.pack()
    frame.focus_set()
    root.mainloop()
  except KeyboardInterrupt as e:
    print "keyboard intterupt"
  finally:
    os.system('xset r on')
    raise KeyboardInterrupt



if __name__ == '__main__':
  main()