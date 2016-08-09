#l a robot usinig python
import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP: 
        stdscr.addstr(2, 20, "Avanzar")
    elif key == curses.KEY_DOWN: 
        stdscr.addstr(4, 20, "Retroceder")

    if key == curses.KEY_LEFT:
        stdscr.addstr(3, 10, "Izq")
    elif key == curses.KEY_RIGHT:
        stdscr.addstr(3, 40, "Der")

    if key == ord('x'):
        stdscr.addstr(7, 10, "Hola mundo")


curses.endwin()
