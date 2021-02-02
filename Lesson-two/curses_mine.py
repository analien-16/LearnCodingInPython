import curses

def window(stdscr):
 # print out message 
 stdscr.addstr("Hello Curses!")
 # collect user information
 stdscr.getch()


curses.wrapper(window)
