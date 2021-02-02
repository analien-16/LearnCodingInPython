import curses
import random

def window(stdscr):

  sh, sw = stdscr.getmaxyx()

  stdscr.nodelay(True)
  stdscr.timeout(100)

  curses.start_color()
  curses.use_default_colors()
  for i in range(0, curses.COLORS):
    curses.init_pair(i +1, i, -1)
    stdscr.addstr("<{0}>".format(i + 1), curses.color_pair(i + 1))
    userKey = stdscr.getch()
    if userKey == 27:
      break

curses.wrapper(window) 