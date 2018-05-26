import curses

from .maze import Maze
from .generators import *
from .printers import utf8_printer


def _main_inner(stdscr):
    stdscr.addstr("Choose maze generation algorithm:\n")
    stdscr.addstr("  1. Breadth First Search\n")
    stdscr.addstr("  2. Depth First Search\n")
    stdscr.addstr("  3. Horizontal Passage\n")
    c = None
    while c != ord('1') and c != ord('2') and c != ord('3'):
        c = stdscr.getch()
    if c == ord('1'):
        generator = bfs_generator
    elif c == ord('2'):
        generator = dfs_generator
    elif c == ord('3'):
        generator = horiz_generator

    width = 39
    height = 23
    m = Maze(width, height, generator, utf8_printer)
    pos = m.initial_position
    x = pos[0]*2
    y = pos[1]

    # Draw the maze
    stdscr.clear()
    stdscr.addstr(str(m))

    while True:
        if y == m.height - 1:
            break  # found the exit

        stdscr.move(y, x)
        c = stdscr.getch()
        if c == curses.KEY_LEFT:
            if x > 0 and not m.get_wall((x-1)//2, y):
                x -= 1
        elif c == curses.KEY_RIGHT:
            if x//2 < width - 1 and not m.get_wall((x+1)//2, y):
                x += 1
        elif c == curses.KEY_UP:
            if y > 0 and not m.get_wall(x//2, y-1):
                y -= 1
        elif c == curses.KEY_DOWN:
            if y < height - 1 and not m.get_wall(x//2, y+1):
                y += 1
        elif c == 27:
            break  # quit the game on Esc key

    if y == m.height-1:
        stdscr.addstr("Congratulations! You found the exit")
        stdscr.getch()


def play():
    curses.wrapper(_main_inner)