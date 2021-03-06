import curses
import random
from curses import textpad

def board(stdscr):
  curses.start_color()
  curses.use_default_colors()
  for i in range(0, curses.COLORS):
    curses.init_pair(i +1, i, -1)
  # turn off the cursor
  curses.curs_set(0)
  stdscr.nodelay(1)
  # timeout in millionsecond
  stdscr.timeout(500)

  # get size of the screen.
  sh, sw = stdscr.getmaxyx()

  welcome_msg = "Welcome to Snake Game!"
  stdscr.addstr(1, sw // 2 - len(welcome_msg) // 2, welcome_msg)

  # define the rectangle box
  box = [
    # top left corner
    [3, 3],
    # bottom right corner
    [sh - 3, sw - 3]
  ]
  # draw the border.
  textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

  # define the snake body.
  snake = [
    # head
    [sh // 2, sw // 2 + 1],
    # body
    [sh // 2, sw // 2],
    # tail
    [sh // 2, sw // 2 - 1]
  ]
  # set the snake body
  snake_ch = chr(9608)

  for point in snake:
    stdscr.addstr(point[0], point[1], snake_ch, curses.color_pair(70))

  # define the direction for snake to move.
  direction = curses.KEY_RIGHT

  # setup a variable for food's location.
  food = [
    random.randint(box[0][0] + 1, box[1][0] - 1),
    random.randint(box[0][1] + 1, box[1][1] - 1)
  ]
  food_ch = "*"
  # paint the food
  stdscr.addstr(food[0], food[1], food_ch)
  
  while True:

    # collect player's keyboard input
    # return -1 if timeout.
    key = stdscr.getch()
    # the ESC key
    if key == 27:
      break

    # decide the snake moving direction based on user's input
    if key == curses.KEY_UP:
      direction = key
    elif key == curses.KEY_DOWN:
      direction = key
    elif key == curses.KEY_LEFT:
      direction = key
    elif key == curses.KEY_RIGHT:
      direction = key

    # try to move the snake to right
    # current head
    head = snake[0]
    # move the snake based on user's input.
    if direction == curses.KEY_UP:
      new_head = [head[0] - 1, head[1]]
    elif direction == curses.KEY_DOWN:
      new_head = [head[0] + 1, head[1]]
    elif direction == curses.KEY_LEFT:
      new_head = [head[0], head[1] - 1]
    elif direction == curses.KEY_RIGHT:
      new_head = [head[0], head[1] + 1]
    # paint the new head  
    stdscr.addstr(new_head[0], new_head[1], snake_ch, curses.color_pair(random.randint(1, 100)))
    # update the snake variable.
    snake.insert(0, new_head)

     # get current tail on board
    tail = snake[-1]
    if new_head == food:
      # grow the snake by NOT erasing the tail
      # generate new food.
      food = [
        random.randint(box[0][0] + 1, box[1][0] - 1),
        random.randint(box[0][1] + 1, box[1][1] - 1)
      ]
      stdscr.addstr(food[0], food[1], food_ch)
    else:
      # erase tail
      stdscr.addstr(tail[0], tail[1], ' ')
      # remove the tail point from the snake variable
      # pop function will pop out (remove) the last item of a list.
      snake.pop()

    # if head of the snake touch any of the border, GAME OVER!
    if (snake[0][0] == box[0][0] or
        snake[0][0] == box[1][0] or
        # left border
        snake[0][1] == box[0][1] or
        # right border
        snake[0][1] == box[1][1]):

        stdscr.addstr(sh // 2, sw // 2, "GAME OVER!")
        stdscr.nodelay(0)
        stdscr.getch()
        break

curses.wrapper(board) 