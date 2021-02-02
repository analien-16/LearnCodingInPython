import curses

def window(stdscr):
  sh, sw = stdscr.getmaxyx()
  stdscr.addstr(sh // 2, sw // 2, "")
  stdscr.addstr(0, 0, "=" * sw)
  # Set-up Colour
  curses.start_color()
  curses.use_default_colors()
  curses.init_pair(127, 127, -1) 
  curses.init_pair(197, 197, -1)
  purple = curses.color_pair(127)
  
  while True:
    
    userKey = stdscr.getch()
    letter = chr(userKey)
    for y in range(0, sh-1):
      stdscr.addstr(y, 0, letter, purple)
      stdscr.addstr(y, sw-1, letter, purple)
    for x in range(0, sw):
      stdscr.addstr(sh-1, x, letter, purple)
      stdscr.addstr(0, x, letter, purple)

    stdscr.addstr(sh // 2, sw // 2, "Code: {0}, Character: {1}".format(userKey, letter))
    if userKey == 27:
      break
      
curses.wrapper(window)





  
 

curses.wrapper(window)